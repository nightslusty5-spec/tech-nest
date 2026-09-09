// PULSE AUDIO - Dynamic Mobile-First Product Engine
document.addEventListener('DOMContentLoaded', function() {
  var state = {
    product: null,
    selectedVariant: null,
    quantity: 1,
    currentImageIndex: 0,
    cartCount: parseInt(localStorage.getItem('pulse_cart_count') || '0', 10)
  };

  updateCartBadge();

  var urlParams = new URLSearchParams(window.location.search);
  var slugParam = urlParams.get('product');
  var pathSegments = window.location.pathname.split('/').filter(Boolean);
  var pathSlug = (pathSegments[0] === 'product' && pathSegments[1]) ? pathSegments[1] : null;
  var productSlug = slugParam || pathSlug || 'pulse-sonic-pro';

  var switcher = document.getElementById('productQuickSwitcher');
  if (switcher) {
    switcher.value = productSlug;
    switcher.addEventListener('change', function(e) {
      window.location.href = '/?product=' + encodeURIComponent(e.target.value);
    });
  }

  loadProductData(productSlug);

  function loadProductData(slug) {
    showSkeleton(true);
    fetch('/api/products/' + encodeURIComponent(slug))
      .then(function(res) {
        if (!res.ok) throw new Error('Product not found');
        return res.json();
      })
      .then(function(prod) {
        state.product = prod;
        state.selectedVariant = prod.variants && prod.variants[0] ? prod.variants[0].id : null;
        state.quantity = 1;
        state.currentImageIndex = 0;
        
        renderProductUI(prod);
        showSkeleton(false);

        if (window.PulseAnalytics) {
          window.PulseAnalytics.trackEvent('ViewContent', {
            content_name: prod.name,
            content_category: prod.category,
            content_ids: [String(prod.id)],
            content_type: 'product',
            value: prod.price,
            currency: 'INR'
          });
        }
      })
      .catch(function(err) {
        console.error('Failed to load product:', err);
        showSkeleton(false);
        showToast('Unable to load product data. Retrying...', 'error');
      });
  }

  function showSkeleton(loading) {
    var skel = document.getElementById('productSkeleton');
    var main = document.getElementById('productMainGrid');
    if (skel) skel.style.display = loading ? 'grid' : 'none';
    if (main) main.style.display = loading ? 'none' : 'grid';
  }

  function renderProductUI(p) {
    document.title = p.name + ' | Official PULSE AUDIO Store';
    var descEl = document.getElementById('seoMetaDesc');
    if (descEl) descEl.setAttribute('content', p.tagline || p.description.substring(0, 160));

    var schemaEl = document.getElementById('productSchemaJson');
    if (schemaEl) {
      schemaEl.textContent = JSON.stringify({
        '@context': 'https://schema.org/',
        '@type': 'Product',
        'name': p.name,
        'image': p.variants && p.variants[0] ? p.variants[0].image : '',
        'description': p.description,
        'brand': { '@type': 'Brand', 'name': p.brand },
        'sku': p.sku,
        'offers': {
          '@type': 'Offer',
          'url': window.location.href,
          'priceCurrency': 'INR',
          'price': p.price,
          'availability': 'https://schema.org/InStock'
        },
        'aggregateRating': {
          '@type': 'AggregateRating',
          'ratingValue': p.rating,
          'reviewCount': p.review_count
        }
      });
    }

    var bCat = document.getElementById('breadcrumbCategory');
    var bName = document.getElementById('breadcrumbProductName');
    if (bCat) bCat.textContent = p.category;
    if (bName) bName.textContent = p.name;

    document.getElementById('productBrand').textContent = p.brand;
    document.getElementById('productSku').textContent = 'SKU: ' + p.sku;
    document.getElementById('productName').textContent = p.name;
    document.getElementById('productTagline').textContent = p.tagline;
    document.getElementById('productRatingVal').textContent = p.rating;
    document.getElementById('productReviewsCount').textContent = p.review_count.toLocaleString('en-IN') + ' Ratings';

    updatePricingUI();
    updateStockUI();
    renderVariants(p.variants);
    renderGallery(p.gallery_images);

    var hlList = document.getElementById('highlightsList');
    if (hlList) {
      hlList.innerHTML = p.highlights.map(function(h) {
        return '<li>' + escapeHtml(h) + '</li>';
      }).join('');
    }

    var descBody = document.getElementById('productFullDescription');
    if (descBody) descBody.textContent = p.description;

    renderSpecifications(p.specifications);

    var boxList = document.getElementById('boxContentsList');
    if (boxList) {
      boxList.innerHTML = p.box_contents.map(function(item) {
        return '<li>✓ ' + escapeHtml(item) + '</li>';
      }).join('');
    }

    var warEl = document.getElementById('warrantyInfoText');
    if (warEl) warEl.textContent = p.warranty_info;

    var faqList = document.getElementById('faqList');
    if (faqList && p.faq) {
      faqList.innerHTML = p.faq.map(function(item) {
        return '<div class="faq-item"><div class="faq-q">Q: ' + escapeHtml(item.q) + '</div><div class="faq-a">' + escapeHtml(item.a) + '</div></div>';
      }).join('');
    }

    renderReviews(p.reviews, p.rating, p.review_count);
  }

  function updatePricingUI() {
    var p = state.product;
    if (!p) return;
    var totalSelling = p.price * state.quantity;
    var totalMrp = p.mrp * state.quantity;

    var elSell = document.getElementById('displaySellingPrice');
    var elMrp = document.getElementById('displayMrpPrice');
    var elDisc = document.getElementById('displayDiscountBadge');
    var elSub = document.getElementById('displayQtySubtotal');
    var elStickyVal = document.getElementById('stickyPriceVal');
    var elStickyMrp = document.getElementById('stickyMrpVal');

    if (elSell) elSell.textContent = totalSelling.toLocaleString('en-IN');
    if (elMrp) elMrp.textContent = '₹' + totalMrp.toLocaleString('en-IN');
    if (elDisc) elDisc.textContent = p.discount_percent + '% OFF';
    if (elSub) elSub.textContent = '₹' + totalSelling.toLocaleString('en-IN');
    if (elStickyVal) elStickyVal.textContent = totalSelling.toLocaleString('en-IN');
    if (elStickyMrp) elStickyMrp.textContent = '₹' + totalMrp.toLocaleString('en-IN');
  }

  function updateStockUI() {
    var p = state.product;
    var banner = document.getElementById('stockStatusBanner');
    var msg = document.getElementById('stockMessage');
    if (!p || !banner || !msg) return;

    var currentVar = getCurrentVariant();
    var stock = currentVar ? currentVar.stock : p.stock;

    if (stock <= 0) {
      banner.className = 'stock-status-banner out';
      msg.textContent = '✕ Currently Out of Stock';
    } else if (stock <= 5) {
      banner.className = 'stock-status-banner low';
      msg.textContent = '⚠️ High Demand: Only ' + stock + ' units left in stock!';
    } else {
      banner.className = 'stock-status-banner';
      msg.textContent = '✓ In Stock (' + stock + ' units available for dispatch)';
    }
  }

  function getCurrentVariant() {
    if (!state.product || !state.product.variants) return null;
    for (var i = 0; i < state.product.variants.length; i++) {
      if (state.product.variants[i].id === state.selectedVariant) {
        return state.product.variants[i];
      }
    }
    return state.product.variants[0];
  }

  function renderVariants(variants) {
    var container = document.getElementById('variantSwatchesGrid');
    if (!container || !variants) return;

    container.innerHTML = variants.map(function(v) {
      var isActive = v.id === state.selectedVariant;
      return `
        <button class="swatch-card ${isActive ? 'active' : ''}" data-variant-id="${v.id}" data-name="${escapeHtml(v.name)}" data-img="${v.image}">
          <div class="swatch-thumb">
            <img src="${v.image}" alt="${escapeHtml(v.name)}">
          </div>
          <div>
            <div class="swatch-name">${escapeHtml(v.name.split('(')[0])}</div>
            <div class="swatch-stock-note">${v.in_stock ? 'In Stock' : 'Sold Out'}</div>
          </div>
        </button>
      `;
    }).join('');

    container.querySelectorAll('.swatch-card').forEach(function(btn) {
      btn.addEventListener('click', function() {
        var vId = btn.getAttribute('data-variant-id');
        var vName = btn.getAttribute('data-name');
        var vImg = btn.getAttribute('data-img');

        state.selectedVariant = vId;
        document.getElementById('selectedVariantLabel').textContent = vName;

        container.querySelectorAll('.swatch-card').forEach(function(c) { c.classList.remove('active'); });
        btn.classList.add('active');

        var mainImg = document.getElementById('mainProductImg');
        if (mainImg && vImg) {
          mainImg.src = vImg;
        }

        updateStockUI();
        showToast('Selected: ' + vName.split('(')[0]);
      });
    });
  }

  function renderGallery(images) {
    if (!images || !images.length) return;
    var desktopStrip = document.getElementById('desktopThumbnails');
    var mobileStrip = document.getElementById('mobileThumbsStrip');
    var dotsContainer = document.getElementById('carouselDots');
    var mainImg = document.getElementById('mainProductImg');

    if (desktopStrip) {
      desktopStrip.innerHTML = images.map(function(img, idx) {
        return `
          <button class="thumb-btn ${idx === 0 ? 'active' : ''}" data-index="${idx}" data-src="${img.url}">
            <img src="${img.url}" alt="${escapeHtml(img.title)}">
          </button>
        `;
      }).join('');

      desktopStrip.querySelectorAll('.thumb-btn').forEach(function(b) {
        b.addEventListener('click', function() {
          var idx = parseInt(b.getAttribute('data-index'), 10);
          switchImage(idx);
        });
      });
    }

    if (mobileStrip) {
      mobileStrip.innerHTML = images.map(function(img, idx) {
        return `
          <button class="mobile-thumb-item ${idx === 0 ? 'active' : ''}" data-index="${idx}">
            <img src="${img.url}" alt="${escapeHtml(img.title)}">
          </button>
        `;
      }).join('');

      mobileStrip.querySelectorAll('.mobile-thumb-item').forEach(function(b) {
        b.addEventListener('click', function() {
          var idx = parseInt(b.getAttribute('data-index'), 10);
          switchImage(idx);
        });
      });
    }

    if (dotsContainer) {
      dotsContainer.innerHTML = images.map(function(_, idx) {
        return `<button class="dot-btn ${idx === 0 ? 'active' : ''}" data-index="${idx}" aria-label="Slide ${idx + 1}"></button>`;
      }).join('');

      dotsContainer.querySelectorAll('.dot-btn').forEach(function(d) {
        d.addEventListener('click', function() {
          var idx = parseInt(d.getAttribute('data-index'), 10);
          switchImage(idx);
        });
      });
    }

    // Touch Swipe Handler for Mobile
    var viewer = document.getElementById('mainImageViewer');
    if (viewer) {
      var touchStartX = 0;
      var touchEndX = 0;

      viewer.addEventListener('touchstart', function(e) {
        touchStartX = e.changedTouches[0].screenX;
      }, { passive: true });

      viewer.addEventListener('touchend', function(e) {
        touchEndX = e.changedTouches[0].screenX;
        var diff = touchEndX - touchStartX;
        if (Math.abs(diff) > 40) {
          if (diff < 0) {
            var nextIdx = (state.currentImageIndex + 1) % images.length;
            switchImage(nextIdx);
          } else {
            var prevIdx = (state.currentImageIndex - 1 + images.length) % images.length;
            switchImage(prevIdx);
          }
        }
      }, { passive: true });

      viewer.addEventListener('mousemove', function(e) {
        if (window.innerWidth < 992) return;
        var rect = viewer.getBoundingClientRect();
        var x = (e.clientX - rect.left) / rect.width;
        var y = (e.clientY - rect.top) / rect.height;
        if (mainImg) {
          mainImg.style.transformOrigin = (x * 100) + '% ' + (y * 100) + '%';
          mainImg.style.transform = 'scale(1.75)';
        }
      });

      viewer.addEventListener('mouseleave', function() {
        if (mainImg) mainImg.style.transform = 'scale(1)';
      });
    }
  }

  function switchImage(index) {
    if (!state.product || !state.product.gallery_images) return;
    var imgs = state.product.gallery_images;
    if (index < 0 || index >= imgs.length) return;
    state.currentImageIndex = index;

    var mainImg = document.getElementById('mainProductImg');
    if (mainImg) mainImg.src = imgs[index].url;

    document.querySelectorAll('.thumb-btn').forEach(function(b, i) {
      b.classList.toggle('active', i === index);
    });
    document.querySelectorAll('.mobile-thumb-item').forEach(function(b, i) {
      b.classList.toggle('active', i === index);
    });
    document.querySelectorAll('.dot-btn').forEach(function(d, i) {
      d.classList.toggle('active', i === index);
    });
  }

  function renderSpecifications(specs) {
    var container = document.getElementById('accBodySpecs');
    if (!container || !specs) return;

    var html = '';
    for (var cat in specs) {
      html += '<div class="specs-category-title">' + escapeHtml(cat) + '</div><div class="specs-grid">';
      for (var key in specs[cat]) {
        html += '<div class="specs-row"><span class="spec-key">' + escapeHtml(key) + '</span><span class="spec-val">' + escapeHtml(specs[cat][key]) + '</span></div>';
      }
      html += '</div>';
    }
    container.innerHTML = html;
  }

  function renderReviews(reviews, rating, count) {
    var scoreVal = document.getElementById('reviewsScoreVal');
    var summaryTotal = document.getElementById('reviewsSummaryTotal');
    if (scoreVal) scoreVal.textContent = rating;
    if (summaryTotal) summaryTotal.textContent = count.toLocaleString('en-IN') + ' Ratings & Reviews';

    var grid = document.getElementById('customerReviewsGrid');
    if (!grid || !reviews) return;

    grid.innerHTML = reviews.map(function(r) {
      var initials = r.name.split(' ').map(function(n) { return n[0]; }).join('').toUpperCase();
      return `
        <div class="review-card">
          <div class="review-user-row">
            <div class="user-avatar">${initials}</div>
            <div>
              <div class="user-name-line">${escapeHtml(r.name)}</div>
              <div class="user-city-tag">✓ Verified Buyer (${escapeHtml(r.city)})</div>
            </div>
          </div>
          <div class="review-rating-row">
            <span class="review-stars">★★★★★</span>
            <span class="review-date">${escapeHtml(r.date)}</span>
            <span class="review-var">Purchased: ${escapeHtml(r.variant)}</span>
          </div>
          <h4 class="review-title">${escapeHtml(r.title)}</h4>
          <p class="review-body">${escapeHtml(r.body)}</p>
        </div>
      `;
    }).join('');
  }

  // Quantity Stepper Handlers
  var btnMinus = document.getElementById('btnQtyMinus');
  var btnPlus = document.getElementById('btnQtyPlus');
  var qtyInput = document.getElementById('qtyInput');
  var qtyWarning = document.getElementById('qtyStockWarning');

  if (btnMinus && btnPlus && qtyInput) {
    btnMinus.addEventListener('click', function() {
      if (state.quantity > 1) {
        state.quantity--;
        qtyInput.value = state.quantity;
        if (qtyWarning) qtyWarning.style.display = 'none';
        updatePricingUI();
      }
    });

    btnPlus.addEventListener('click', function() {
      var curVar = getCurrentVariant();
      var maxStock = curVar ? curVar.stock : (state.product ? state.product.stock : 10);
      if (state.quantity < maxStock && state.quantity < 5) {
        state.quantity++;
        qtyInput.value = state.quantity;
        if (qtyWarning) qtyWarning.style.display = 'none';
        updatePricingUI();
      } else {
        if (qtyWarning) {
          qtyWarning.textContent = state.quantity >= maxStock 
            ? 'Maximum available stock limit reached (' + maxStock + ' units).' 
            : 'Maximum limit of 5 units per order.';
          qtyWarning.style.display = 'block';
        }
      }
    });
  }

  // Copy Coupon Code Handler
  var copyBtn = document.getElementById('btnCopyCoupon');
  if (copyBtn) {
    copyBtn.addEventListener('click', function() {
      var code = copyBtn.getAttribute('data-coupon') || 'PREPAID100';
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(code);
      }
      copyBtn.textContent = 'COPIED!';
      copyBtn.style.background = '#059669';
      copyBtn.style.color = '#ffffff';
      showToast('✓ Coupon ' + code + ' copied to clipboard! ₹100 Off applied.');
      setTimeout(function() {
        copyBtn.textContent = 'COPY';
        copyBtn.style.background = '';
        copyBtn.style.color = '';
      }, 2500);
    });
  }

  // PIN Code Delivery Checker Handler
  var pinBtn = document.getElementById('btnPincodeCheck');
  var pinInput = document.getElementById('pincodeInput');
  var pinFeedback = document.getElementById('pincodeFeedback');

  if (pinBtn && pinInput && pinFeedback) {
    pinBtn.addEventListener('click', function() {
      var pin = pinInput.value.trim();
      if (pin.length !== 6 || isNaN(pin)) {
        pinFeedback.className = 'pincode-feedback error';
        pinFeedback.textContent = 'Please enter a valid 6-digit Indian PIN code.';
        pinFeedback.style.display = 'block';
        return;
      }

      pinBtn.textContent = 'Checking...';
      fetch('/api/checkout/check-pincode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pincode: pin })
      })
      .then(function(r) { return r.json(); })
      .then(function(data) {
        pinBtn.textContent = 'CHECK';
        pinFeedback.className = 'pincode-feedback ' + (data.serviceable ? 'success' : 'error');
        pinFeedback.textContent = data.message;
        pinFeedback.style.display = 'block';
      })
      .catch(function() {
        pinBtn.textContent = 'CHECK';
        pinFeedback.className = 'pincode-feedback error';
        pinFeedback.textContent = 'Unable to check PIN code right now. Try again.';
        pinFeedback.style.display = 'block';
      });
    });
  }

  // Accordion Expand/Collapse Logic
  document.querySelectorAll('.accordion-header').forEach(function(header) {
    header.addEventListener('click', function() {
      var item = header.parentElement;
      var body = item.querySelector('.accordion-body');
      var isOpen = body.classList.contains('active');

      if (isOpen) {
        body.classList.remove('active');
        item.classList.remove('open');
        header.setAttribute('aria-expanded', 'false');
      } else {
        body.classList.add('active');
        item.classList.add('open');
        header.setAttribute('aria-expanded', 'true');
      }
    });
  });

  // Add to Cart Handlers
  var addCartBtns = [
    document.getElementById('desktopAddCartBtn'),
    document.getElementById('mobileStickyAddCartBtn')
  ].filter(Boolean);

  addCartBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      state.cartCount++;
      localStorage.setItem('pulse_cart_count', state.cartCount);
      updateCartBadge();
      showToast('🛒 Added ' + state.quantity + 'x ' + (state.product ? state.product.name : 'item') + ' to your cart!', 'success');

      if (window.PulseAnalytics && state.product) {
        window.PulseAnalytics.trackEvent('AddToCart', {
          content_name: state.product.name,
          content_ids: [String(state.product.id)],
          content_type: 'product',
          value: state.product.price * state.quantity,
          currency: 'INR'
        });
      }
    });
  });

  // Buy Now Handlers (Redirect to Checkout)
  var buyNowBtns = [
    document.getElementById('desktopBuyNowBtn'),
    document.getElementById('mobileStickyBuyBtn')
  ].filter(Boolean);

  buyNowBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      if (!state.product) return;
      var eventId = window.PulseAnalytics ? window.PulseAnalytics.generateEventId('ic') : 'evt_' + Date.now();
      
      sessionStorage.setItem('pulse_checkout_product', JSON.stringify({
        productId: state.product.id,
        productSlug: state.product.slug,
        productName: state.product.name,
        variantId: state.selectedVariant,
        quantity: state.quantity,
        price: state.product.price,
        mrp: state.product.mrp,
        eventId: eventId
      }));

      window.location.href = '/checkout.html?product=' + encodeURIComponent(state.product.slug) + '&variant=' + encodeURIComponent(state.selectedVariant) + '&qty=' + state.quantity;
    });
  });

  // Fullscreen Lightbox Modal
  var btnFs = document.getElementById('btnFullscreenModal');
  var lbModal = document.getElementById('lightboxModal');
  var lbClose = document.getElementById('btnLightboxClose');
  var lbImg = document.getElementById('lightboxImg');
  var lbCap = document.getElementById('lightboxCaption');

  if (btnFs && lbModal && lbClose && lbImg) {
    btnFs.addEventListener('click', function() {
      if (!state.product || !state.product.gallery_images) return;
      var cur = state.product.gallery_images[state.currentImageIndex];
      lbImg.src = cur.url;
      if (lbCap) lbCap.textContent = cur.caption || state.product.name;
      lbModal.style.display = 'flex';
    });

    lbClose.addEventListener('click', function() { lbModal.style.display = 'none'; });
    lbModal.addEventListener('click', function(e) {
      if (e.target === lbModal) lbModal.style.display = 'none';
    });
  }

  function updateCartBadge() {
    var badge = document.getElementById('cartCountBadge');
    if (badge) badge.textContent = state.cartCount;
  }

  function showToast(text, type) {
    var container = document.getElementById('toastContainer');
    if (!container) return;
    var toast = document.createElement('div');
    toast.className = 'toast-msg ' + (type || '');
    toast.textContent = text;
    container.appendChild(toast);
    setTimeout(function() { toast.remove(); }, 3000);
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }
});
