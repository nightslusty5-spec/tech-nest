// PULSE AUDIO - Dynamic Mobile-First Product Engine
document.addEventListener('DOMContentLoaded', function() {

  var DEFAULT_CATALOGUE = {
    'pulse-sonic-pro': {
      id: 1,
      slug: 'pulse-sonic-pro',
      name: 'Pulse Sonic Pro ANC True Wireless Earbuds',
      tagline: '35dB Hybrid Active Noise Cancellation • 13mm Titanium Drivers • 40H Monster Battery',
      price: 1499.0,
      mrp: 2999.0,
      discount_percent: 50,
      stock: 28,
      rating: 4.8,
      review_count: 14820,
      category: 'Audio & Wearables',
      description: 'Experience studio-grade acoustic clarity and deep cinematic bass with the Pulse Sonic Pro ANC True Wireless Earbuds. Designed for discerning audiophiles and daily commuters, these earbuds feature advanced 35dB Hybrid Active Noise Cancellation that blocks out ambient drone, traffic noise, and background chatter.',
      highlights: [
        '35dB Hybrid Active Noise Cancellation with Transparency Mode',
        '13mm Titanium-Coated Dynamic Acoustic Drivers for punchy bass',
        '40 Hours Combined Playtime (8 Hours in earbuds + 32 Hours case)',
        '45ms Ultra-Low Latency Dedicated Beast Gaming Mode',
        'IPX4 Water & Sweat Resistance with nano-coating',
        'Quad-Mic ENC (Environmental Noise Cancellation) for crystal clear HD calls'
      ],
      specifications: {
        'Audio & Acoustics': {
          'Driver Size': '13mm Titanium Composite Diaphragm',
          'Noise Cancellation': '35dB Hybrid ANC + Quad-Mic ENC',
          'Frequency Response': '20Hz - 20,000Hz',
          'Latency': '45ms Dedicated Gaming Mode'
        },
        'Connectivity & Power': {
          'Bluetooth Version': 'v5.3 + EDR (Instant Auto-Pairing)',
          'Operating Range': '10 - 15 Meters',
          'Total Playtime': 'Up to 40 Hours with Charging Case',
          'Charging Interface': 'Type-C ASAP Fast Charge (10 min = 3 hrs)'
        },
        'Build & Durability': {
          'Water Resistance': 'IPX4 Splash & Sweat Proof',
          'Earbud Weight': '3.8g per earbud (Ultra Featherweight)'
        }
      },
      box_contents: [
        '1 Pair of Pulse Sonic Pro ANC Earbuds',
        '1x Fast-Charging Pocket Storage Case',
        '3x Ergonomic Silicone Eartips (S / M / L)',
        '1x Braided USB Type-C Fast Charging Cable',
        '1x User Manual & 1-Year Official Warranty Card'
      ],
      warranty_info: '1-Year Official Brand Doorstep Replacement Warranty. Free courier pickup across all Indian PIN codes.',
      faq: [
        { q: 'Is Active Noise Cancellation (ANC) real or software-based?', a: 'Pulse Sonic Pro uses dedicated dual-feedforward and feedback microphones with a hardware DSP chip to provide real 35dB hybrid acoustic noise cancellation.' },
        { q: 'How is the microphone quality for calling in noisy outdoor areas?', a: 'It features Quad-Mic Environmental Noise Cancellation (ENC) that isolates your voice from traffic and wind.' },
        { q: 'Does it support fast charging?', a: 'Yes! Our ASAP Fast Charge technology gives you 3 hours of playback with just 10 minutes of charging via Type-C.' },
        { q: 'Is Cash on Delivery available?', a: 'To ensure fastest express courier priority delivery, orders are pre-paid via Instant UPI, Google Pay, PhonePe, Paytm, and Cards with an instant ₹100 discount.' }
      ],
      variants: [
        { id: 'midnight-obsidian', name: 'Midnight Obsidian (Matte Black)', color_code: '#18181b', in_stock: true, stock: 12, image_url: '/assets/images/earbuds-black.svg' },
        { id: 'arctic-frost', name: 'Arctic Frost (Pure Pearl White)', color_code: '#f8fafc', in_stock: true, stock: 9, image_url: '/assets/images/earbuds-white.svg' },
        { id: 'forest-emerald', name: 'Forest Emerald (Deep Matte Green)', color_code: '#064e3b', in_stock: true, stock: 7, image_url: '/assets/images/earbuds-green.svg' }
      ],
      gallery_images: [
        { url: '/assets/images/earbuds-black.svg', caption: 'Pulse Sonic Pro ANC - Midnight Obsidian', alt_text: 'Front view of earbuds with charging case' },
        { url: '/assets/images/earbuds-green.svg', caption: 'Pulse Sonic Pro - Forest Emerald Edition', alt_text: 'Emerald green variant earbuds' },
        { url: '/assets/images/earbuds-white.svg', caption: 'Pulse Sonic Pro - Arctic Frost Edition', alt_text: 'Pearl white earbuds' },
        { url: '/assets/images/earbuds-anc.svg', caption: '35dB Hybrid Active Noise Cancellation Architecture', alt_text: 'ANC noise canceling visual' },
        { url: '/assets/images/earbuds-driver.svg', caption: '13mm Custom Titanium Bass Drivers', alt_text: 'Titanium driver diagram' },
        { url: '/assets/images/earbuds-ipx4.svg', caption: 'IPX4 Water & Sweat Resistance Coating', alt_text: 'IPX4 waterproof test' },
        { url: '/assets/images/earbuds-lifestyle.svg', caption: 'Ergonomic In-Ear Fit for All-Day Comfort', alt_text: 'Lifestyle in-ear fit' }
      ],
      reviews: [
        { name: 'Rohan Deshmukh', city: 'Pune', rating: 5, date: '04 Sep 2026', variant: 'Midnight Obsidian', title: 'Better sound & ANC than ₹4,000 earbuds!', body: 'Honestly surprised by the bass depth and ANC. On the metro ride it canceled out most of the track rumbling. Battery easily lasts 4-5 days with my case usage.' },
        { name: 'Priya Sundaram', city: 'Chennai', rating: 5, date: '02 Sep 2026', variant: 'Arctic Frost', title: 'Crystal clear mic and super comfy', body: 'I take 4-5 hours of Zoom & Teams meetings daily. Everyone hears me loud and clear. Very comfortable in small ears.' },
        { name: 'Vikram Malhotra', city: 'Gurugram', rating: 5, date: '28 Aug 2026', variant: 'Forest Emerald', title: 'The emerald green color is breathtaking!', body: 'Matte texture feels very premium in hand. 45ms gaming mode is noticeable with zero lag in BGMI.' }
      ]
    },
    'pulse-hypercharge-33w': {
      id: 2,
      slug: 'pulse-hypercharge-33w',
      name: 'Pulse HyperCharge 33W GaN Dual-Port Fast Charger',
      tagline: 'Gallium Nitride (GaN III) • Type-C PD 3.0 + USB-A Quick Charge • Ultra-Compact',
      price: 899.0,
      mrp: 1999.0,
      discount_percent: 55,
      stock: 42,
      rating: 4.9,
      review_count: 8640,
      category: 'Power & Charging',
      description: 'Power up your smartphones, tablets, and accessories at blazing speeds with the Pulse HyperCharge 33W GaN Dual-Port Fast Charger.',
      highlights: [
        'Next-Gen GaN III Semiconductor Technology for cool and efficient charging',
        'Dual Output: 33W USB-C Power Delivery 3.0 + 18W USB-A QC 3.0',
        'Charges iPhone & Android up to 60% in just 30 minutes',
        'Universal Compatibility with smartphones, earbuds, tablets, and smartwatches',
        'Multi-Layer Smart Protection against over-voltage and short circuit'
      ],
      specifications: {
        'Power Output': {
          'Total Wattage': '33W Max',
          'USB-C Port': '5V/3A, 9V/3A, 11V/3A, 12V/2.5A, 20V/1.5A (33W Max)',
          'USB-A Port': '5V/3A, 9V/2A, 12V/1.5A (18W Max)',
          'Dual Port Simultaneous': '5V/4A Shared'
        }
      },
      box_contents: [
        '1x Pulse HyperCharge 33W GaN Adapter',
        '1x Quick Start Guide & 1-Year Warranty Card'
      ],
      warranty_info: '1-Year Official Brand Doorstep Replacement Warranty.',
      faq: [
        { q: 'Will this fast charge my iPhone / Samsung?', a: 'Yes! It supports full PD 3.0 and PPS protocols for high-speed charging of iPhones, Samsungs, OnePluses, and Pixels.' }
      ],
      variants: [
        { id: 'stealth-black', name: 'Stealth Black (Matte)', color_code: '#18181b', in_stock: true, stock: 24, image_url: '/assets/images/charger-black.svg' },
        { id: 'ice-white', name: 'Ice White (Glossy)', color_code: '#f8fafc', in_stock: true, stock: 18, image_url: '/assets/images/charger-white.svg' }
      ],
      gallery_images: [
        { url: '/assets/images/charger-black.svg', caption: 'Pulse HyperCharge 33W GaN - Stealth Black', alt_text: 'Dual-port 33W fast charger' },
        { url: '/assets/images/charger-white.svg', caption: 'Pulse HyperCharge 33W GaN - Ice White', alt_text: 'White edition 33W charger' }
      ],
      reviews: [
        { name: 'Amit Verma', city: 'Delhi', rating: 5, date: '01 Sep 2026', variant: 'Stealth Black', title: 'Compact beast!', body: 'Smaller than my thumb and charges my phone from 15% to 70% in half an hour without heating.' }
      ]
    },
    'pulse-powermax-20k': {
      id: 3,
      slug: 'pulse-powermax-20k',
      name: 'Pulse PowerMax 20000mAh 22.5W Fast Power Bank',
      tagline: '20000mAh Lithium-Polymer • 22.5W Two-Way Fast Charge • Triple Output Ports',
      price: 1699.0,
      mrp: 3499.0,
      discount_percent: 51,
      stock: 35,
      rating: 4.7,
      review_count: 5120,
      category: 'Power & Charging',
      description: 'Never run out of power with the Pulse PowerMax 20000mAh Power Bank.',
      highlights: [
        'Massive 20,000mAh High-Density Li-Polymer Battery Capacity',
        '22.5W Super Fast Charging with PD 3.0 & QC 3.0 Protocols',
        'Triple Device Charging (2x USB-A + 1x Type-C Input/Output)',
        'Smart LED Digital Battery Percentage Display'
      ],
      specifications: {
        'Battery Specs': {
          'Capacity': '20,000mAh / 74Wh',
          'Output Ports': '2x USB-A (22.5W) + 1x Type-C (20W PD)'
        }
      },
      box_contents: [
        '1x Pulse PowerMax 20000mAh Power Bank',
        '1x Type-C Charging Cable',
        '1x User Manual & Warranty Card'
      ],
      warranty_info: '1-Year Official Brand Replacement Warranty.',
      faq: [
        { q: 'Is this flight-safe in cabin baggage?', a: 'Yes, 74Wh is compliant with DGCA and FAA guidelines for carry-on cabin baggage.' }
      ],
      variants: [
        { id: 'space-black', name: 'Space Black (Textured Grip)', color_code: '#18181b', in_stock: true, stock: 35, image_url: '/assets/images/powerbank-black.svg' }
      ],
      gallery_images: [
        { url: '/assets/images/powerbank-black.svg', caption: 'Pulse PowerMax 20000mAh 22.5W Power Bank', alt_text: '20000mAh power bank' }
      ],
      reviews: [
        { name: 'Kavita Rao', city: 'Bengaluru', rating: 5, date: '29 Aug 2026', variant: 'Space Black', title: 'Charges my phone 4.5 times!', body: 'Solid build with numeric LED screen. Super fast 22.5W charging.' }
      ]
    },
    'pulse-armorcable-c': {
      id: 4,
      slug: 'pulse-armorcable-c',
      name: 'Pulse ArmorCable 100W Braided Type-C to Type-C Fast Cable (1.5m)',
      tagline: '100W Power Delivery E-Marker Chip • Military-Grade Nylon Braiding • 480Mbps Data',
      price: 399.0,
      mrp: 999.0,
      discount_percent: 60,
      stock: 85,
      rating: 4.8,
      review_count: 9230,
      category: 'Cables & Accessories',
      description: 'Engineered for extreme durability and ultra-high power delivery.',
      highlights: [
        'Supports 100W (20V/5A) Power Delivery Fast Charging',
        'Integrated E-Marker Smart Chip for safe current regulation',
        'Double-Braided Military-Grade Ballistic Nylon Jacket',
        'Tested to withstand 25,000+ extreme 90-degree bends'
      ],
      specifications: {
        'Cable Details': {
          'Max Wattage': '100W (20V / 5A)',
          'Length': '1.5 Meters (5 Feet)',
          'Data Transfer Speed': '480 Mbps USB 2.0'
        }
      },
      box_contents: [
        '1x Pulse ArmorCable 100W Braided Type-C Cable (1.5m)',
        '1x Reusable Cable Organizer Tie'
      ],
      warranty_info: '2-Year Official Brand Replacement Warranty.',
      faq: [
        { q: 'Can this cable charge MacBooks and laptops?', a: 'Yes! It handles up to 100W PD charging for MacBooks, Dell XPS, HP laptops, and smartphones.' }
      ],
      variants: [
        { id: 'braided-black', name: 'Braided Obsidian Black', color_code: '#18181b', in_stock: true, stock: 85, image_url: '/assets/images/cable-black.svg' }
      ],
      gallery_images: [
        { url: '/assets/images/cable-black.svg', caption: 'Pulse ArmorCable 100W Braided Type-C Cable', alt_text: '100W fast charging cable' }
      ],
      reviews: [
        { name: 'Siddharth Nair', city: 'Kochi', rating: 5, date: '03 Sep 2026', variant: 'Braided Obsidian Black', title: 'Indestructible cable', body: 'The thick braiding and aluminum connectors are top quality. Charges my laptop and phone at max speed.' }
      ]
    }
  };

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

  // Pre-load default instant catalogue immediately so UI renders in 0ms
  var initialProd = DEFAULT_CATALOGUE[productSlug] || DEFAULT_CATALOGUE['pulse-sonic-pro'];
  state.product = initialProd;
  state.selectedVariant = initialProd.variants && initialProd.variants[0] ? initialProd.variants[0].id : null;
  renderProductUI(initialProd);

  // Then fetch live dynamic updates from backend
  loadProductData(productSlug);

  function loadProductData(slug) {
    fetch('/api/products/' + encodeURIComponent(slug))
      .then(function(res) {
        if (!res.ok) throw new Error('Product not found');
        return res.json();
      })
      .then(function(prod) {
        state.product = prod;
        if (!state.selectedVariant && prod.variants && prod.variants[0]) {
          state.selectedVariant = prod.variants[0].id;
        }
        renderProductUI(prod);

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
        console.log('Using instant cached product model');
      });
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
        'description': p.description,
        'brand': { '@type': 'Brand', 'name': 'PULSE AUDIO' },
        'offers': {
          '@type': 'Offer',
          'priceCurrency': 'INR',
          'price': p.price,
          'availability': p.stock > 0 ? 'https://schema.org/InStock' : 'https://schema.org/OutOfStock'
        }
      });
    }

    var elName = document.getElementById('displayProductName');
    var elTag = document.getElementById('displayProductTagline');
    var elCat = document.getElementById('breadcrumbCategory');
    var elBcName = document.getElementById('breadcrumbProductName');
    var elSku = document.getElementById('displaySkuCode');

    if (elName) elName.textContent = p.name;
    if (elTag) elTag.textContent = p.tagline;
    if (elCat) elCat.textContent = p.category;
    if (elBcName) elBcName.textContent = p.name;
    if (elSku) elSku.textContent = (p.sku || ('SKU-PULSE-' + p.id));

    var elRating = document.getElementById('displayRatingScore');
    var elCount = document.getElementById('displayReviewCount');
    if (elRating) elRating.textContent = p.rating || '4.8';
    if (elCount) elCount.textContent = '(' + (p.review_count ? p.review_count.toLocaleString('en-IN') : '14,820') + ' Verified Reviews)';

    var elStock = document.getElementById('liveStockBadge');
    if (elStock) {
      if (p.stock && p.stock <= 30) {
        elStock.textContent = '🔥 Only ' + p.stock + ' Units Left in Stock';
        elStock.className = 'stock-pill urgency';
      } else {
        elStock.textContent = '✓ In Stock • Ready to Dispatch';
        elStock.className = 'stock-pill available';
      }
    }

    updatePricingUI();
    renderVariants(p.variants);
    renderGallery(p.gallery_images);
    renderHighlights(p.highlights);
    renderBoxContents(p.box_contents);
    renderSpecifications(p.specifications);
    renderFaq(p.faq);
    renderReviews(p.reviews, p.rating, p.review_count);

    var elDesc = document.getElementById('productFullDescription');
    if (elDesc) elDesc.textContent = p.description;

    var elWarranty = document.getElementById('warrantyInfoText');
    if (elWarranty && p.warranty_info) elWarranty.textContent = p.warranty_info;
  }

  function updatePricingUI() {
    if (!state.product) return;
    var p = state.product;
    var sellingEl = document.getElementById('displaySellingPrice');
    var mrpEl = document.getElementById('displayMrpPrice');
    var discEl = document.getElementById('displayDiscountBadge');
    var subtotalEl = document.getElementById('displayQtySubtotal');
    var stickyPrice = document.getElementById('stickyPriceVal');
    var stickyMrp = document.getElementById('stickyMrpVal');

    var unitPrice = p.price;
    var unitMrp = p.mrp;
    var discount = p.discount_percent || Math.round(((unitMrp - unitPrice) / unitMrp) * 100);
    var subtotal = unitPrice * state.quantity;

    if (sellingEl) sellingEl.textContent = unitPrice.toLocaleString('en-IN');
    if (mrpEl) mrpEl.textContent = '₹' + unitMrp.toLocaleString('en-IN');
    if (discEl) discEl.textContent = discount + '% OFF';
    if (subtotalEl) subtotalEl.textContent = '₹' + subtotal.toLocaleString('en-IN');
    if (stickyPrice) stickyPrice.textContent = (unitPrice * state.quantity).toLocaleString('en-IN');
    if (stickyMrp) stickyMrp.textContent = '₹' + (unitMrp * state.quantity).toLocaleString('en-IN');
  }

  function renderVariants(variants) {
    var container = document.getElementById('variantSwatchesGrid');
    var label = document.getElementById('selectedVariantLabel');
    if (!container || !variants || variants.length === 0) return;

    container.innerHTML = variants.map(function(v) {
      var isSelected = (v.id === state.selectedVariant);
      var isLight = v.color_code.toLowerCase() === '#f8fafc' || v.color_code.toLowerCase() === '#ffffff';
      return `
        <button class="variant-swatch-card ${isSelected ? 'active' : ''}" data-variant-id="${v.id}" aria-label="${v.name}">
          <span class="color-dot ${isLight ? 'border-light' : ''}" style="background-color: ${v.color_code};"></span>
          <span class="variant-name">${v.name.split('(')[0].trim()}</span>
          ${!v.in_stock ? '<span class="out-badge">Out</span>' : ''}
        </button>
      `;
    }).join('');

    var activeVar = variants.find(function(v) { return v.id === state.selectedVariant; }) || variants[0];
    if (label && activeVar) label.textContent = activeVar.name;

    container.querySelectorAll('.variant-swatch-card').forEach(function(card) {
      card.addEventListener('click', function() {
        var vId = card.getAttribute('data-variant-id');
        selectVariant(vId);
      });
    });
  }

  function selectVariant(variantId) {
    if (!state.product || !state.product.variants) return;
    state.selectedVariant = variantId;
    var v = state.product.variants.find(function(item) { return item.id === variantId; });
    var label = document.getElementById('selectedVariantLabel');
    if (label && v) label.textContent = v.name;

    document.querySelectorAll('.variant-swatch-card').forEach(function(card) {
      card.classList.toggle('active', card.getAttribute('data-variant-id') === variantId);
    });

    if (v && v.image_url) {
      var mainImg = document.getElementById('mainProductImg');
      if (mainImg) mainImg.src = v.image_url;
    }
  }

  function renderGallery(images) {
    if (!images || images.length === 0) return;
    var thumbsCol = document.getElementById('desktopThumbnailsCol');
    var mobileScroll = document.getElementById('mobileThumbsScroll');
    var dotsContainer = document.getElementById('galleryDotsContainer');
    var mainImg = document.getElementById('mainProductImg');

    if (mainImg && images[0]) {
      mainImg.src = images[0].url;
      mainImg.alt = images[0].alt_text || state.product.name;
    }

    if (thumbsCol) {
      thumbsCol.innerHTML = images.map(function(img, idx) {
        return `
          <button class="thumb-btn ${idx === 0 ? 'active' : ''}" data-index="${idx}" aria-label="Thumbnail ${idx + 1}">
            <img src="${img.url}" alt="${img.alt_text || 'Thumbnail'}">
          </button>
        `;
      }).join('');
      thumbsCol.querySelectorAll('.thumb-btn').forEach(function(btn) {
        btn.addEventListener('click', function() { switchImage(parseInt(btn.getAttribute('data-index'), 10)); });
      });
    }

    if (mobileScroll) {
      mobileScroll.innerHTML = images.map(function(img, idx) {
        return `
          <div class="mobile-thumb-item ${idx === 0 ? 'active' : ''}" data-index="${idx}">
            <img src="${img.url}" alt="${img.alt_text || 'Thumbnail'}">
          </div>
        `;
      }).join('');
      mobileScroll.querySelectorAll('.mobile-thumb-item').forEach(function(item) {
        item.addEventListener('click', function() { switchImage(parseInt(item.getAttribute('data-index'), 10)); });
      });
    }

    if (dotsContainer) {
      dotsContainer.innerHTML = images.map(function(img, idx) {
        return `<button class="dot-btn ${idx === 0 ? 'active' : ''}" data-index="${idx}" aria-label="Slide ${idx + 1}"></button>`;
      }).join('');
      dotsContainer.querySelectorAll('.dot-btn').forEach(function(dot) {
        dot.addEventListener('click', function() { switchImage(parseInt(dot.getAttribute('data-index'), 10)); });
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

    document.querySelectorAll('.thumb-btn').forEach(function(b, i) { b.classList.toggle('active', i === index); });
    document.querySelectorAll('.mobile-thumb-item').forEach(function(b, i) { b.classList.toggle('active', i === index); });
    document.querySelectorAll('.dot-btn').forEach(function(d, i) { d.classList.toggle('active', i === index); });
  }

  function renderHighlights(highlights) {
    var container = document.getElementById('highlightsList');
    if (!container || !highlights) return;
    container.innerHTML = highlights.map(function(h) {
      return `<li><span class="bullet-bolt">⚡</span><span>${escapeHtml(h)}</span></li>`;
    }).join('');
  }

  function renderBoxContents(items) {
    var container = document.getElementById('boxContentsList');
    if (!container || !items) return;
    container.innerHTML = items.map(function(it) {
      return `<li><span class="box-icon">📦</span><span>${escapeHtml(it)}</span></li>`;
    }).join('');
  }

  function renderFaq(faqList) {
    var container = document.getElementById('faqList');
    if (!container || !faqList) return;
    container.innerHTML = faqList.map(function(item) {
      return `
        <div class="faq-item">
          <div class="faq-question"><strong>Q:</strong> ${escapeHtml(item.q)}</div>
          <div class="faq-answer"><strong>A:</strong> ${escapeHtml(item.a)}</div>
        </div>
      `;
    }).join('');
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
    if (scoreVal) scoreVal.textContent = rating || '4.8';
    if (summaryTotal) summaryTotal.textContent = (count || 14820).toLocaleString('en-IN') + ' Ratings & Reviews';

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
      if (state.quantity < 5) {
        state.quantity++;
        qtyInput.value = state.quantity;
        if (qtyWarning) qtyWarning.style.display = 'none';
        updatePricingUI();
      } else {
        if (qtyWarning) {
          qtyWarning.textContent = 'Maximum limit of 5 units per order.';
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
      pinFeedback.className = 'pincode-feedback success';
      pinFeedback.textContent = '✓ Express Delivery Available for PIN ' + pin + ' (Expected in 2-3 business days) • Online Payment Only';
      pinFeedback.style.display = 'block';
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

  // Master Buy Now Function (Instant Checkout Redirect)
  function handleBuyNowClick(e) {
    if (e && e.preventDefault) e.preventDefault();
    var prod = state.product || DEFAULT_CATALOGUE['pulse-sonic-pro'];
    var curVar = state.selectedVariant || (prod.variants && prod.variants[0] ? prod.variants[0].id : 'midnight-obsidian');
    var qty = state.quantity || 1;
    var eventId = window.PulseAnalytics ? window.PulseAnalytics.generateEventId('ic') : 'evt_' + Date.now();

    sessionStorage.setItem('pulse_checkout_product', JSON.stringify({
      productId: prod.id || 1,
      productSlug: prod.slug || 'pulse-sonic-pro',
      productName: prod.name || 'Pulse Sonic Pro ANC True Wireless Earbuds',
      variantId: curVar,
      quantity: qty,
      price: prod.price || 1499.0,
      mrp: prod.mrp || 2999.0,
      eventId: eventId
    }));

    window.location.href = '/checkout.html?product=' + encodeURIComponent(prod.slug || 'pulse-sonic-pro') + '&variant=' + encodeURIComponent(curVar) + '&qty=' + qty;
  }

  // Master Add to Cart Function
  function handleAddToCartClick(e) {
    if (e && e.preventDefault) e.preventDefault();
    var prod = state.product || DEFAULT_CATALOGUE['pulse-sonic-pro'];
    state.cartCount++;
    localStorage.setItem('pulse_cart_count', state.cartCount);
    updateCartBadge();
    showToast('🛒 Added ' + state.quantity + 'x ' + prod.name + ' to cart!', 'success');

    if (window.PulseAnalytics) {
      window.PulseAnalytics.trackEvent('AddToCart', {
        content_name: prod.name,
        content_ids: [String(prod.id)],
        content_type: 'product',
        value: prod.price * state.quantity,
        currency: 'INR'
      });
    }
  }

  // Attach to all Buy Now Buttons
  var buyNowIds = ['desktopBuyNowBtn', 'mobileStickyBuyBtn'];
  buyNowIds.forEach(function(id) {
    var el = document.getElementById(id);
    if (el) {
      el.addEventListener('click', handleBuyNowClick);
    }
  });

  // Attach to all Add to Cart Buttons
  var addCartIds = ['desktopAddCartBtn', 'mobileStickyAddCartBtn'];
  addCartIds.forEach(function(id) {
    var el = document.getElementById(id);
    if (el) {
      el.addEventListener('click', handleAddToCartClick);
    }
  });

  // Global delegation fallback for any button marked with buy-now classes
  document.addEventListener('click', function(e) {
    var target = e.target.closest('#desktopBuyNowBtn, #mobileStickyBuyBtn, .btn-buy-now, .btn-desktop-buy-now, .btn-sticky-buy-now');
    if (target) {
      handleBuyNowClick(e);
    }
  });

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
