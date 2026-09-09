# Clean Frontend Writer
import os

def write_files():
    # 1. index.html
    with open('frontend/index.html', 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title id="seoPageTitle">Pulse Sonic Pro ANC True Wireless Earbuds | PULSE AUDIO</title>
  <meta id="seoMetaDesc" name="description" content="Official PULSE AUDIO Store: 35dB Hybrid ANC Earbuds with 13mm Titanium Drivers, 40-hour monster battery, and 45ms gaming mode.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700;800&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="/css/style.css">
  <link rel="stylesheet" href="/css/product.css">
  <link rel="stylesheet" href="/css/responsive.css">
  
  <!-- Dynamic OpenGraph & JSON-LD Container -->
  <script type="application/ld+json" id="productSchemaJson"></script>
  <!-- Meta Pixel SDK -->
  <script src="/js/meta-pixel.js"></script>
</head>
<body class="light-theme">

  <!-- Toast Notification Container -->
  <div id="toastContainer" class="toast-container" aria-live="polite"></div>

  <!-- Top Announcement Promo Bar -->
  <div class="top-announcement-bar">
    <div class="container announcement-inner">
      <div class="announcement-badge">⚡ META LAUNCH DEAL</div>
      <span class="announcement-text">
        Get Flat <strong>₹100 Instant Discount</strong> with code <code id="headerCouponCode">PREPAID100</code> | Free Express Delivery across India 🇮🇳
      </span>
    </div>
  </div>

  <!-- Compact Mobile-First Header -->
  <header class="site-header">
    <div class="container header-inner">
      <!-- Brand Logo -->
      <a href="/" class="brand-logo" id="headerLogoLink">
        <div class="logo-symbol">⚡</div>
        <div class="logo-text">
          <span class="brand-name">PULSE</span>
          <span class="brand-sub">AUDIO</span>
        </div>
      </a>

      <!-- Product Quick Switcher (For Multi-Product Meta Ads) -->
      <div class="product-quick-nav">
        <select id="productQuickSwitcher" class="product-switcher-select" aria-label="Switch Product">
          <option value="pulse-sonic-pro" selected>🎧 Pulse Sonic Pro ANC Earbuds (₹1,499)</option>
          <option value="pulse-hypercharge-33w">⚡ 33W GaN Dual Fast Charger (₹899)</option>
          <option value="pulse-powermax-20k">🔋 20000mAh 22.5W Power Bank (₹1,699)</option>
          <option value="pulse-armorcable-c">🔌 100W Braided Type-C Cable (₹399)</option>
        </select>
      </div>

      <!-- Header Actions -->
      <div class="header-actions">
        <div class="header-trust-tag hide-mobile">
          <span class="trust-icon">🛡️</span>
          <span>1 Year Warranty</span>
        </div>

        <button class="cart-action-btn" id="headerCartBtn" aria-label="Shopping Cart">
          <span class="cart-icon">🛒</span>
          <span class="cart-count-badge" id="cartCountBadge">0</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Breadcrumb Bar (Desktop & Tablet) -->
  <nav class="breadcrumb-container hide-mobile" aria-label="Breadcrumb">
    <div class="container">
      <ol class="breadcrumb-list">
        <li><a href="/">Home</a></li>
        <li class="sep">›</li>
        <li><span id="breadcrumbCategory">Audio &amp; Wearables</span></li>
        <li class="sep">›</li>
        <li class="active" id="breadcrumbProductName">Pulse Sonic Pro ANC</li>
      </ol>
    </div>
  </nav>

  <!-- Main Product Landing Container -->
  <main class="container product-main-container">
    
    <!-- Dynamic Skeleton Loader -->
    <div id="productSkeleton" class="skeleton-layout" style="display: none;">
      <div class="skeleton-gallery-box skeleton-pulse"></div>
      <div class="skeleton-info-col">
        <div class="skeleton-line title skeleton-pulse"></div>
        <div class="skeleton-line sub skeleton-pulse"></div>
        <div class="skeleton-line price skeleton-pulse"></div>
        <div class="skeleton-line btn skeleton-pulse"></div>
      </div>
    </div>

    <!-- Main Dynamic Product Grid -->
    <div id="productMainGrid" class="product-main-grid">
      
      <!-- ================= LEFT COLUMN: INTERACTIVE GALLERY ================= -->
      <div class="product-gallery-column">
        <div class="gallery-sticky-wrapper">
          
          <!-- Gallery Viewport & Thumbnails -->
          <div class="gallery-main-viewport-row">
            
            <!-- Desktop Vertical Thumbnails -->
            <div class="thumbnail-strip hide-mobile" id="desktopThumbnails"></div>

            <!-- Main Interactive Display -->
            <div class="main-image-viewer" id="mainImageViewer">
              <div class="bestseller-badge-pill" id="productBadgeTag">🔥 #1 BESTSELLER</div>
              
              <!-- Image element -->
              <img id="mainProductImg" src="/assets/images/earbuds-black.svg" alt="Product Image" loading="eager">

              <!-- Zoom hint for desktop -->
              <div class="zoom-hint hide-mobile">
                <span>🔍 Hover to zoom • Click to expand</span>
              </div>

              <!-- Fullscreen Button -->
              <button class="btn-fullscreen-trigger" id="btnFullscreenModal" aria-label="View Fullscreen">
                ⤢
              </button>
            </div>
          </div>

          <!-- Mobile Swipe Indicator Dots & Thumbnails -->
          <div class="mobile-gallery-controls show-mobile">
            <div class="carousel-dots-row" id="carouselDots"></div>
            <div class="mobile-thumbs-scroll" id="mobileThumbsStrip"></div>
          </div>

          <!-- Desktop CTA Action Buttons -->
          <div class="desktop-cta-actions hide-mobile">
            <button class="btn-action btn-desktop-add-cart" id="desktopAddCartBtn">
              <span class="btn-icon">🛒</span>
              <span>ADD TO CART</span>
            </button>
            <button class="btn-action btn-desktop-buy-now" id="desktopBuyNowBtn">
              <span class="btn-icon">⚡</span>
              <span>BUY NOW</span>
            </button>
          </div>

          <!-- Security Seals -->
          <div class="trust-seals-grid">
            <div class="seal-item">
              <span class="seal-icon">🔒</span>
              <span class="seal-text">256-Bit SSL Encrypted</span>
            </div>
            <div class="seal-item">
              <span class="seal-icon">⚡</span>
              <span class="seal-text">Razorpay Instant UPI</span>
            </div>
            <div class="seal-item">
              <span class="seal-icon">🛡️</span>
              <span class="seal-text">1-Year Doorstep Warranty</span>
            </div>
            <div class="seal-item">
              <span class="seal-icon">🔄</span>
              <span class="seal-text">7 Days Replacement</span>
            </div>
          </div>

        </div>
      </div>

      <!-- ================= RIGHT COLUMN: DYNAMIC PRODUCT DETAILS ================= -->
      <div class="product-info-column">
        
        <!-- Brand & Title Block -->
        <div class="product-title-block">
          <div class="brand-row">
            <span class="brand-badge-pill" id="productBrand">PULSE AUDIO</span>
            <span class="sku-tag" id="productSku">SKU: PA-TW3500-BLK</span>
          </div>
          <h1 class="product-title-heading" id="productName">Pulse Sonic Pro ANC True Wireless Earbuds</h1>
          <p class="product-tagline" id="productTagline">35dB Hybrid ANC • 13mm Titanium Drivers • 40H Monster Battery • 45ms Gaming</p>
        </div>

        <!-- Rating Summary & Real-time Live Demand -->
        <div class="rating-demand-row">
          <div class="rating-pill-green">
            <span id="productRatingVal">4.8</span>
            <span class="star-char">★</span>
          </div>
          <span class="reviews-count-text" id="productReviewsCount">14,820 Verified Ratings</span>
          <span class="verified-store-tag">✓ Verified Store</span>
        </div>

        <!-- Dynamic Stock Status Indicator -->
        <div class="stock-status-banner" id="stockStatusBanner">
          <span class="stock-indicator-dot"></span>
          <span class="stock-message" id="stockMessage">✓ In Stock (28 units available)</span>
        </div>

        <!-- High-Impact Price Box -->
        <div class="price-deal-card">
          <div class="price-header-row">
            <span class="price-currency">₹</span>
            <span class="price-selling" id="displaySellingPrice">1,499</span>
            <span class="price-mrp" id="displayMrpPrice">₹2,999</span>
            <span class="price-discount-pill" id="displayDiscountBadge">50% OFF</span>
          </div>
          <div class="price-sub-info">
            <span class="tax-note">Inclusive of all taxes</span>
            <span class="bullet-sep">•</span>
            <span class="shipping-note text-green">FREE Express Insured Delivery</span>
          </div>
        </div>

        <!-- Dynamic Offers & Copyable Coupons Section -->
        <div class="offers-container">
          <div class="offers-header">
            <span class="icon">🏷️</span>
            <strong>Available Offers &amp; Instant Coupons</strong>
          </div>

          <div class="offer-cards-list">
            <!-- Coupon Card with Copy Action -->
            <div class="coupon-item-card highlight">
              <div class="coupon-left-col">
                <div class="coupon-code-chip" id="couponChip">PREPAID100</div>
                <p class="coupon-desc">Flat <strong>₹100 Instant Discount</strong> on prepaid orders (UPI / Cards). Applied automatically at checkout.</p>
              </div>
              <button class="btn-copy-coupon" id="btnCopyCoupon" data-coupon="PREPAID100" aria-label="Copy Coupon">
                COPY
              </button>
            </div>

            <!-- Bank Cashback Offer -->
            <div class="coupon-item-card">
              <div class="coupon-left-col">
                <div class="bank-tag-chip">BANK OFFER</div>
                <p class="coupon-desc">5% Unlimited Cashback on HDFC, Axis &amp; ICICI Bank Credit Cards.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Dynamic Color / Variant Swatch Selector -->
        <div class="variants-selection-section">
          <div class="variants-header-row">
            <span class="variant-heading">Select Color:</span>
            <strong class="selected-variant-label" id="selectedVariantLabel">Midnight Obsidian (Matte Black)</strong>
          </div>
          
          <div class="variant-swatches-grid" id="variantSwatchesGrid"></div>
        </div>

        <!-- Dynamic Quantity Stepper & Subtotal -->
        <div class="quantity-stepper-section">
          <div class="qty-header-row">
            <span class="qty-heading">Quantity:</span>
            <div class="qty-stepper-box">
              <button class="btn-qty-step" id="btnQtyMinus" aria-label="Decrease quantity">−</button>
              <input type="number" id="qtyInput" class="qty-input" value="1" min="1" max="10" readonly>
              <button class="btn-qty-step" id="btnQtyPlus" aria-label="Increase quantity">+</button>
            </div>
          </div>
          <div class="qty-subtotal-info">
            <span>Item Subtotal:</span>
            <strong class="subtotal-val" id="displayQtySubtotal">₹1,499</strong>
          </div>
          <div id="qtyStockWarning" class="qty-stock-warning" style="display: none;"></div>
        </div>

        <!-- Pincode Delivery Availability Checker -->
        <div class="pincode-card">
          <div class="pincode-title-row">
            <span class="pin-icon">📍</span>
            <span class="pin-title">Check Delivery Date &amp; COD Availability</span>
          </div>
          <div class="pincode-input-group">
            <input type="text" id="pincodeInput" placeholder="Enter 6-digit PIN code (e.g. 110001, 560038)" maxlength="6">
            <button class="btn-pincode-check" id="btnPincodeCheck">CHECK</button>
          </div>
          <div id="pincodeFeedback" class="pincode-feedback" style="display: none;"></div>
        </div>

        <!-- Key Feature Highlights Grid -->
        <div class="feature-highlights-box">
          <h3 class="highlights-heading">⚡ Key Highlights</h3>
          <ul class="highlights-list" id="highlightsList"></ul>
        </div>

        <!-- Mobile-Friendly Collapsible Accordions -->
        <div class="accordions-container">
          
          <!-- Accordion 1: Description -->
          <div class="accordion-item" data-accordion="desc">
            <button class="accordion-header" aria-expanded="true">
              <span class="acc-title">📖 Product Overview &amp; Experience</span>
              <span class="acc-icon">▾</span>
            </button>
            <div class="accordion-body active" id="accBodyDesc">
              <p id="productFullDescription">Experience studio-grade acoustic clarity and deep cinematic bass...</p>
            </div>
          </div>

          <!-- Accordion 2: Full Specifications -->
          <div class="accordion-item" data-accordion="specs">
            <button class="accordion-header" aria-expanded="false">
              <span class="acc-title">📋 Full Technical Specifications</span>
              <span class="acc-icon">▾</span>
            </button>
            <div class="accordion-body" id="accBodySpecs"></div>
          </div>

          <!-- Accordion 3: What's in the Box -->
          <div class="accordion-item" data-accordion="box">
            <button class="accordion-header" aria-expanded="false">
              <span class="acc-title">📦 What's In The Box</span>
              <span class="acc-icon">▾</span>
            </button>
            <div class="accordion-body" id="accBodyBox">
              <ul class="box-contents-list" id="boxContentsList"></ul>
            </div>
          </div>

          <!-- Accordion 4: Warranty & Guarantees -->
          <div class="accordion-item" data-accordion="warranty">
            <button class="accordion-header" aria-expanded="false">
              <span class="acc-title">🛡️ 1-Year Doorstep Warranty &amp; Authenticity</span>
              <span class="acc-icon">▾</span>
            </button>
            <div class="accordion-body" id="accBodyWarranty">
              <p id="warrantyInfoText">1 Year Official Pulse Brand Replacement Warranty with Free Doorstep Pickup Support.</p>
              <p class="warranty-sub">To register or claim warranty, simply scan the included card or email <strong>support@pulse-audio.in</strong>.</p>
            </div>
          </div>

          <!-- Accordion 5: Frequently Asked Questions -->
          <div class="accordion-item" data-accordion="faq">
            <button class="accordion-header" aria-expanded="false">
              <span class="acc-title">❓ Frequently Asked Questions</span>
              <span class="acc-icon">▾</span>
            </button>
            <div class="accordion-body" id="accBodyFaq">
              <div class="faq-list" id="faqList"></div>
            </div>
          </div>

        </div>

      </div>
    </div>

    <!-- ================= VERIFIED CUSTOMER REVIEWS SECTION ================= -->
    <section class="reviews-section" id="reviewsSection">
      <div class="reviews-section-header">
        <div>
          <h2 class="reviews-main-title">Verified Customer Reviews</h2>
          <p class="reviews-sub-title">100% Real purchases from customers across India</p>
        </div>
      </div>

      <!-- Rating Breakdown Card -->
      <div class="reviews-summary-card">
        <div class="score-col">
          <div class="big-score"><span id="reviewsScoreVal">4.8</span> <span class="star">★</span></div>
          <p class="total-ratings-text" id="reviewsSummaryTotal">14,820 Ratings &amp; 3,240 Reviews</p>
          <span class="recommend-tag">⚡ 96% of buyers recommend this product</span>
        </div>

        <div class="bars-col">
          <div class="rating-bar-row"><span class="star-label">5 ★</span><div class="bar-bg"><div class="bar-fill" style="width:84%;"></div></div><span class="pct">84%</span></div>
          <div class="rating-bar-row"><span class="star-label">4 ★</span><div class="bar-bg"><div class="bar-fill" style="width:11%;"></div></div><span class="pct">11%</span></div>
          <div class="rating-bar-row"><span class="star-label">3 ★</span><div class="bar-bg"><div class="bar-fill" style="width:3%;"></div></div><span class="pct">3%</span></div>
          <div class="rating-bar-row"><span class="star-label">2 ★</span><div class="bar-bg"><div class="bar-fill" style="width:1%;"></div></div><span class="pct">1%</span></div>
          <div class="rating-bar-row"><span class="star-label">1 ★</span><div class="bar-bg"><div class="bar-fill" style="width:1%;"></div></div><span class="pct">1%</span></div>
        </div>
      </div>

      <!-- Reviews Cards List -->
      <div class="customer-reviews-grid" id="customerReviewsGrid"></div>
    </section>

  </main>

  <!-- ================= STORE FOOTER ================= -->
  <footer class="site-footer">
    <div class="container footer-inner">
      <div class="footer-col-brand">
        <div class="brand-logo">
          <div class="logo-symbol">⚡</div>
          <div class="logo-text">
            <span class="brand-name">PULSE</span>
            <span class="brand-sub">AUDIO</span>
          </div>
        </div>
        <p class="footer-desc">India's leading consumer audio &amp; smart gadget electronics brand. Engineered for high-fidelity acoustics, ultra-fast charging, and long-lasting durability.</p>
        <div class="payment-badges-row">
          <span class="badge-chip">UPI</span>
          <span class="badge-chip">GPay</span>
          <span class="badge-chip">PhonePe</span>
          <span class="badge-chip">Paytm</span>
          <span class="badge-chip">Visa</span>
          <span class="badge-chip">Mastercard</span>
          <span class="badge-chip">Razorpay</span>
        </div>
      </div>

      <div class="footer-col-links">
        <h4>Customer Care</h4>
        <ul>
          <li><a href="/checkout.html">Track Order</a></li>
          <li><a href="#accBodyWarranty">1-Year Warranty Claim</a></li>
          <li><a href="#">7-Day Replacement Terms</a></li>
          <li><a href="#">Express Delivery Policy</a></li>
        </ul>
      </div>

      <div class="footer-col-links">
        <h4>Company</h4>
        <ul>
          <li><a href="#">About PULSE AUDIO</a></li>
          <li><a href="#">Privacy Policy</a></li>
          <li><a href="#">Terms of Service</a></li>
          <li><a href="#">Support Contact</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom-bar">
      <div class="container footer-bottom-flex">
        <p>© 2026 PULSE AUDIO Innovations Pvt Ltd. All Rights Reserved.</p>
        <p class="sec-text">🔒 256-Bit SSL Encrypted &amp; Verified Indian Merchant</p>
      </div>
    </div>
  </footer>

  <!-- ================= MOBILE STICKY BOTTOM PURCHASE BAR ================= -->
  <div class="mobile-sticky-buy-bar" id="mobileStickyBar">
    <div class="sticky-price-info">
      <div class="sticky-price-row">
        <span class="curr">₹</span>
        <span class="val" id="stickyPriceVal">1,499</span>
        <span class="mrp" id="stickyMrpVal">₹2,999</span>
      </div>
      <span class="shipping-tag">Free Express Shipping</span>
    </div>
    
    <div class="sticky-buttons-row">
      <button class="btn-sticky-add-cart" id="mobileStickyAddCartBtn" aria-label="Add to cart">
        🛒
      </button>
      <button class="btn-sticky-buy-now" id="mobileStickyBuyBtn">
        <span>⚡ BUY NOW</span>
      </button>
    </div>
  </div>

  <!-- ================= FULLSCREEN LIGHTBOX MODAL ================= -->
  <div id="lightboxModal" class="lightbox-modal" style="display: none;">
    <button class="btn-lightbox-close" id="btnLightboxClose" aria-label="Close Fullscreen">✕</button>
    <div class="lightbox-content">
      <img id="lightboxImg" src="" alt="Fullscreen Image">
      <p id="lightboxCaption" class="lightbox-caption"></p>
    </div>
  </div>

  <script src="/js/app.js"></script>
</body>
</html>
''')
    print('Wrote frontend/index.html')

    # 2. Checkout HTML
    with open('frontend/checkout.html', 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Secure Checkout | PULSE AUDIO</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700;800&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="/css/style.css">
  <link rel="stylesheet" href="/css/checkout.css">
  <link rel="stylesheet" href="/css/responsive.css">
  <script src="/js/meta-pixel.js"></script>
  <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
</head>
<body class="light-theme checkout-page">

  <!-- Header -->
  <header class="checkout-header">
    <div class="container checkout-header-inner">
      <a href="/" class="brand-logo">
        <div class="logo-symbol">⚡</div>
        <div class="logo-text">
          <span class="brand-name">PULSE</span>
          <span class="brand-sub">AUDIO</span>
        </div>
      </a>
      <div class="checkout-security-tag">
        <span class="lock-icon">🔒</span>
        <span>100% Safe &amp; Secure Checkout</span>
      </div>
    </div>
  </header>

  <!-- Checkout Main Container -->
  <main class="container checkout-container">
    <div class="checkout-grid">
      
      <!-- Left Column: Shipping & Customer Details Form -->
      <div class="checkout-form-column">
        <div class="checkout-card">
          <div class="checkout-card-header">
            <span class="step-num">1</span>
            <h2>Shipping &amp; Delivery Address</h2>
          </div>

          <form id="checkoutAddressForm" class="checkout-form" novalidate>
            <div class="form-row">
              <div class="form-group">
                <label for="custName">Full Name <span class="req">*</span></label>
                <input type="text" id="custName" placeholder="e.g. Aditya Sharma" required value="Aditya Sharma">
              </div>
            </div>

            <div class="form-row two-col">
              <div class="form-group">
                <label for="custPhone">Mobile Number (for delivery tracking) <span class="req">*</span></label>
                <div class="phone-input-wrap">
                  <span class="country-code">+91</span>
                  <input type="tel" id="custPhone" placeholder="9876543210" maxlength="10" required value="9876543210">
                </div>
              </div>

              <div class="form-group">
                <label for="custEmail">Email Address (for invoice &amp; tracking) <span class="req">*</span></label>
                <input type="email" id="custEmail" placeholder="aditya.sharma@example.com" required value="aditya.sharma@gmail.com">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="custAddress">Street Address / House No. / Building <span class="req">*</span></label>
                <input type="text" id="custAddress" placeholder="Flat 402, Sunshine Heights, 100 Feet Ring Road" required value="Flat 402, Sunshine Heights, 100 Feet Ring Road">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="custApartment">Landmark / Area (Optional)</label>
                <input type="text" id="custApartment" placeholder="Near Indiranagar Metro Station" value="Near Indiranagar Metro Station">
              </div>
            </div>

            <div class="form-row three-col">
              <div class="form-group">
                <label for="custPincode">PIN Code <span class="req">*</span></label>
                <input type="text" id="custPincode" placeholder="560038" maxlength="6" required value="560038">
              </div>

              <div class="form-group">
                <label for="custCity">City / Town <span class="req">*</span></label>
                <input type="text" id="custCity" placeholder="Bengaluru" required value="Bengaluru">
              </div>

              <div class="form-group">
                <label for="custState">State <span class="req">*</span></label>
                <select id="custState" required>
                  <option value="Karnataka" selected>Karnataka</option>
                  <option value="Maharashtra">Maharashtra</option>
                  <option value="Delhi">Delhi NCR</option>
                  <option value="Tamil Nadu">Tamil Nadu</option>
                  <option value="Telangana">Telangana</option>
                  <option value="Uttar Pradesh">Uttar Pradesh</option>
                  <option value="Gujarat">Gujarat</option>
                  <option value="West Bengal">West Bengal</option>
                  <option value="Kerala">Kerala</option>
                  <option value="Rajasthan">Rajasthan</option>
                  <option value="Other">Other State</option>
                </select>
              </div>
            </div>

            <!-- Payment Option Preview -->
            <div class="payment-method-selector">
              <h3 class="selector-title">
                <span class="step-num">2</span> Payment Method
              </h3>
              
              <div class="payment-card-option selected">
                <div class="option-radio">
                  <input type="radio" id="payOnline" name="paymentMethod" value="razorpay" checked>
                  <label for="payOnline">
                    <strong>Razorpay Instant UPI / Cards / NetBanking</strong>
                    <span class="option-badge">Instant ₹100 Discount</span>
                  </label>
                </div>
                <div class="payment-sub-logos">
                  <span>⚡ GPay, PhonePe, Paytm, BHIM UPI, All Major Cards &amp; Netbanking</span>
                </div>
              </div>
            </div>

            <div class="submit-action-row">
              <button type="submit" class="btn-proceed-pay" id="proceedPayBtn">
                <span>🔒</span> PROCEED TO PAYMENT
              </button>
            </div>
          </form>
        </div>
      </div>

      <!-- Right Column: Dynamic Order Summary -->
      <div class="checkout-summary-column">
        <div class="summary-card-sticky">
          <h3 class="summary-title">Order Summary</h3>

          <div class="summary-product-row">
            <div class="summary-img-box">
              <img id="summaryProdImg" src="/assets/images/earbuds-black.svg" alt="Product Image">
            </div>
            <div class="summary-info">
              <h4 class="prod-name" id="summaryProdName">Pulse Sonic Pro ANC True Wireless Earbuds</h4>
              <p class="variant-tag" id="summaryVariantName">Variant: Midnight Obsidian</p>
              <div class="qty-price-row">
                <span class="qty-badge" id="summaryQtyBadge">Qty: 1</span>
                <span class="price-strong" id="summaryUnitPrice">₹1,499</span>
                <span class="mrp-striked" id="summaryUnitMrp">₹2,999</span>
              </div>
            </div>
          </div>

          <!-- Coupon Card -->
          <div class="applied-coupon-box">
            <div class="coupon-left">
              <span class="coupon-icon">🏷️</span>
              <div>
                <strong>PREPAID100</strong>
                <p class="coupon-msg">₹100 instant prepaid discount applied</p>
              </div>
            </div>
            <span class="coupon-tag-success">✓ APPLIED</span>
          </div>

          <!-- Price Calculation Rows -->
          <div class="price-breakdown">
            <div class="price-row">
              <span>Item MRP:</span>
              <span class="strike" id="summaryTotalMrp">₹2,999</span>
            </div>
            <div class="price-row">
              <span>Special Selling Price:</span>
              <span id="summarySubtotal">₹1,499</span>
            </div>
            <div class="price-row discount-row">
              <span>Prepaid Discount (PREPAID100):</span>
              <span id="summaryDiscount" class="text-green">-₹100</span>
            </div>
            <div class="price-row">
              <span>Express Insured Shipping:</span>
              <span class="text-green">FREE</span>
            </div>
            <div class="price-divider"></div>
            <div class="price-row total-row">
              <strong>Total Payable Amount:</strong>
              <strong class="grand-total" id="summaryTotal">₹1,399</strong>
            </div>
          </div>

          <!-- Guarantee badges -->
          <div class="summary-trust-perks">
            <div class="trust-perk">
              <span class="icon">🛡️</span>
              <span>1 Year Official Replacement Warranty</span>
            </div>
            <div class="trust-perk">
              <span class="icon">🔄</span>
              <span>7 Days Easy Replacement</span>
            </div>
            <div class="trust-perk">
              <span class="icon">⚡</span>
              <span>Instant Dispatch within 24 Hours</span>
            </div>
          </div>
        </div>
      </div>

    </div>
  </main>

  <script src="/js/checkout.js"></script>
</body>
</html>
''')
    print('Wrote frontend/checkout.html')

    # 3. Success HTML
    with open('frontend/success.html', 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Order Confirmed | PULSE AUDIO</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700;800&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="/css/style.css">
  <link rel="stylesheet" href="/css/checkout.css">
  <link rel="stylesheet" href="/css/responsive.css">
  <script src="/js/meta-pixel.js"></script>
</head>
<body class="light-theme success-page">

  <header class="checkout-header">
    <div class="container checkout-header-inner">
      <a href="/" class="brand-logo">
        <div class="logo-symbol">⚡</div>
        <div class="logo-text">
          <span class="brand-name">PULSE</span>
          <span class="brand-sub">AUDIO</span>
        </div>
      </a>
      <span class="order-placed-pill">✓ Payment Verified</span>
    </div>
  </header>

  <main class="container success-container">
    <div class="success-card">
      <div class="success-animation-badge">
        <div class="checkmark-circle">✓</div>
      </div>
      
      <h1 class="success-title">Thank You For Your Order!</h1>
      <p class="success-subtitle">Your order has been received and is being prepared for express dispatch.</p>

      <div class="order-ref-pill">
        <span>Order Reference Number:</span>
        <strong id="orderIdDisplay">PULSE-ORD-LOADING</strong>
      </div>

      <!-- Order Tracking Stepper -->
      <div class="tracking-stepper">
        <div class="step-node active">
          <div class="node-dot">✓</div>
          <span class="node-label">Order Confirmed</span>
        </div>
        <div class="step-connector active"></div>
        <div class="step-node active">
          <div class="node-dot">⚡</div>
          <span class="node-label">Payment Verified</span>
        </div>
        <div class="step-connector"></div>
        <div class="step-node">
          <div class="node-dot">📦</div>
          <span class="node-label">Dispatched</span>
        </div>
        <div class="step-connector"></div>
        <div class="step-node">
          <div class="node-dot">🚚</div>
          <span class="node-label">Out for Delivery</span>
        </div>
      </div>

      <!-- Receipt Grid -->
      <div class="receipt-card-grid">
        <div class="receipt-section">
          <h3>Customer Details</h3>
          <p><strong id="orderCustName">Aditya Sharma</strong></p>
          <p id="orderPhone">+91 9876543210</p>
        </div>

        <div class="receipt-section">
          <h3>Shipping Address</h3>
          <p id="orderAddress">Flat 402, Sunshine Heights, Bengaluru, Karnataka - 560038</p>
        </div>

        <div class="receipt-section">
          <h3>Ordered Item</h3>
          <p><strong id="orderProdName">Pulse Sonic Pro ANC Earbuds</strong></p>
          <p id="orderVariant">Variant: Midnight Obsidian</p>
        </div>

        <div class="receipt-section">
          <h3>Payment &amp; Delivery</h3>
          <p>Amount Paid: <strong class="text-green" id="orderAmount">₹1,399</strong></p>
          <p>Est. Delivery: <strong id="orderDeliveryEst">3-5 business days</strong></p>
        </div>
      </div>

      <div class="warranty-card-box">
        <span class="box-icon">🛡️</span>
        <div>
          <h4>1-Year Official Doorstep Warranty Activated</h4>
          <p>Your electronic warranty card and GST tax invoice have been sent to your registered email address.</p>
        </div>
      </div>

      <div class="success-actions-row">
        <a href="/" class="btn-continue-shopping">← Return to Store</a>
        <button class="btn-print-receipt" onclick="window.print()">🖨️ Print Invoice</button>
      </div>
    </div>
  </main>

  <script src="/js/success.js"></script>
</body>
</html>
''')
    print('Wrote frontend/success.html')

    # 4. Checkout JS
    with open('frontend/js/checkout.js', 'w', encoding='utf-8') as f:
        f.write('''// PULSE AUDIO - Dynamic Checkout & Payment Gateway Engine
document.addEventListener('DOMContentLoaded', function() {
  var urlParams = new URLSearchParams(window.location.search);
  var sessionItem = JSON.parse(sessionStorage.getItem('pulse_checkout_product') || 'null');

  var checkoutState = sessionItem || {
    productId: 1,
    productSlug: 'pulse-sonic-pro',
    productName: 'Pulse Sonic Pro ANC True Wireless Earbuds',
    variantId: urlParams.get('variant') || 'midnight-obsidian',
    quantity: parseInt(urlParams.get('qty') || '1', 10),
    price: 1499.0,
    mrp: 2999.0,
    eventId: 'ic_' + Date.now()
  };

  var appliedCoupon = 'PREPAID100';
  var couponDiscount = 100.0;

  // If slug was passed in URL, fetch dynamic product details to sync price
  var slugFromUrl = urlParams.get('product') || checkoutState.productSlug;
  if (slugFromUrl) {
    fetch('/api/products/' + encodeURIComponent(slugFromUrl))
      .then(function(r) { return r.json(); })
      .then(function(prod) {
        checkoutState.productId = prod.id;
        checkoutState.productName = prod.name;
        checkoutState.price = prod.price;
        checkoutState.mrp = prod.mrp;
        updateSummary();
      })
      .catch(function() {
        updateSummary();
      });
  } else {
    updateSummary();
  }

  // Track Meta Pixel InitiateCheckout
  if (window.PulseAnalytics) {
    window.PulseAnalytics.trackEvent('InitiateCheckout', {
      content_name: checkoutState.productName,
      content_ids: [String(checkoutState.productId)],
      content_type: 'product',
      value: (checkoutState.price * checkoutState.quantity) - couponDiscount,
      currency: 'INR',
      num_items: checkoutState.quantity
    }, checkoutState.eventId);
  }

  function updateSummary() {
    var subtotal = checkoutState.price * checkoutState.quantity;
    var mrpTotal = checkoutState.mrp * checkoutState.quantity;
    var finalTotal = Math.max(1, subtotal - couponDiscount);

    var elProdName = document.getElementById('summaryProdName');
    var elVar = document.getElementById('summaryVariantName');
    var elQty = document.getElementById('summaryQtyBadge');
    var elUnitP = document.getElementById('summaryUnitPrice');
    var elUnitMrp = document.getElementById('summaryUnitMrp');
    var elTotMrp = document.getElementById('summaryTotalMrp');
    var elSub = document.getElementById('summarySubtotal');
    var elDisc = document.getElementById('summaryDiscount');
    var elTot = document.getElementById('summaryTotal');
    var elBtn = document.getElementById('proceedPayBtn');

    if (elProdName) elProdName.textContent = checkoutState.productName;
    if (elVar) elVar.textContent = 'Variant: ' + (checkoutState.variantId || 'Standard');
    if (elQty) elQty.textContent = 'Qty: ' + checkoutState.quantity;
    if (elUnitP) elUnitP.textContent = '₹' + checkoutState.price.toLocaleString('en-IN');
    if (elUnitMrp) elUnitMrp.textContent = '₹' + checkoutState.mrp.toLocaleString('en-IN');
    if (elTotMrp) elTotMrp.textContent = '₹' + mrpTotal.toLocaleString('en-IN');
    if (elSub) elSub.textContent = '₹' + subtotal.toLocaleString('en-IN');
    if (elDisc) elDisc.textContent = '-₹' + couponDiscount.toLocaleString('en-IN');
    if (elTot) elTot.textContent = '₹' + finalTotal.toLocaleString('en-IN');
    if (elBtn) elBtn.innerHTML = '<span>🔒</span> PROCEED TO PAYMENT (₹' + finalTotal.toLocaleString('en-IN') + ')';
  }

  // Address Form Submission
  var form = document.getElementById('checkoutAddressForm');
  var btn = document.getElementById('proceedPayBtn');

  if (form) {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      var name = document.getElementById('custName').value.trim();
      var phone = document.getElementById('custPhone').value.trim();
      var email = document.getElementById('custEmail').value.trim();
      var addr = document.getElementById('custAddress').value.trim();
      var apt = document.getElementById('custApartment').value.trim();
      var city = document.getElementById('custCity').value.trim();
      var state = document.getElementById('custState').value;
      var pin = document.getElementById('custPincode').value.trim();

      if (!name || !phone || !email || !addr || !city || !state || !pin) {
        alert('Please fill all required delivery details.');
        return;
      }

      if (phone.length < 10) {
        alert('Please enter a valid 10-digit mobile number.');
        return;
      }

      btn.disabled = true;
      btn.innerHTML = '<span>⏳</span> Initializing Secure Payment Gateway...';

      var payload = {
        product_id: checkoutState.productId,
        variant_id: checkoutState.variantId,
        quantity: checkoutState.quantity,
        coupon_code: appliedCoupon,
        customer_name: name,
        phone: phone,
        email: email,
        address: addr,
        apartment: apt,
        city: city,
        state: state,
        pincode: pin,
        event_id: checkoutState.eventId
      };

      fetch('/api/checkout/create-order', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
      .then(function(r) {
        if (!r.ok) throw new Error('Order creation failed');
        return r.json();
      })
      .then(function(orderData) {
        openRazorpay(orderData);
      })
      .catch(function(err) {
        console.error(err);
        btn.disabled = false;
        updateSummary();
        alert('Unable to initiate checkout. Please try again.');
      });
    });
  }

  function openRazorpay(orderData) {
    if (window.Razorpay && !orderData.is_mock) {
      var opt = {
        key: orderData.key_id,
        amount: orderData.amount * 100,
        currency: 'INR',
        name: 'PULSE AUDIO Official',
        description: checkoutState.productName,
        order_id: orderData.razorpay_order_id,
        prefill: {
          name: orderData.customer_name,
          email: orderData.email,
          contact: orderData.phone
        },
        theme: { color: '#4f46e5' },
        handler: function(resp) {
          verifyPayment(orderData.order_number, resp.razorpay_order_id, resp.razorpay_payment_id, resp.razorpay_signature);
        },
        modal: {
          ondismiss: function() {
            btn.disabled = false;
            updateSummary();
          }
        }
      };
      var rzp = new window.Razorpay(opt);
      rzp.open();
    } else {
      renderSandbox(orderData);
    }
  }

  function renderSandbox(orderData) {
    var existingModal = document.getElementById('sandboxModal');
    if (existingModal) existingModal.remove();

    var modal = document.createElement('div');
    modal.id = 'sandboxModal';
    modal.className = 'sandbox-modal-backdrop';
    modal.innerHTML = `
      <div class="sandbox-modal-card">
        <div class="sandbox-badge">RAZORPAY SECURE GATEWAY (SANDBOX SIMULATOR)</div>
        <div class="sandbox-brand">
          <span class="brand-bolt">⚡</span>
          <strong>PULSE AUDIO Official Store</strong>
        </div>
        <p class="sandbox-order-no">Order Reference: <strong>${orderData.order_number}</strong></p>
        <div class="sandbox-payable-row">
          <span>Amount Payable (Post Discount):</span>
          <strong class="payable-amt">₹${orderData.amount.toLocaleString('en-IN')}</strong>
        </div>
        <div class="sandbox-methods">
          <div class="method-chip active">UPI (GPay / PhonePe / Paytm)</div>
          <div class="method-chip">Cards & Netbanking</div>
        </div>
        <button id="mockSuccessBtn" class="sandbox-pay-btn">
          <span>🔒</span> SIMULATE SUCCESSFUL PAYMENT
        </button>
        <button id="mockCloseBtn" class="sandbox-cancel-btn">Cancel Transaction</button>
      </div>
    `;
    document.body.appendChild(modal);

    document.getElementById('mockSuccessBtn').onclick = function() {
      this.textContent = 'Verifying Server Signature (HMAC-SHA256)...';
      this.disabled = true;
      verifyPayment(orderData.order_number, orderData.razorpay_order_id, 'pay_mock_' + Date.now(), 'sandbox_success_sig');
    };

    document.getElementById('mockCloseBtn').onclick = function() {
      modal.remove();
      btn.disabled = false;
      updateSummary();
    };
  }

  function verifyPayment(ordNum, rzpOrdId, rzpPayId, rzpSig) {
    fetch('/api/checkout/verify-payment', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        order_number: ordNum,
        razorpay_order_id: rzpOrdId,
        razorpay_payment_id: rzpPayId,
        razorpay_signature: rzpSig
      })
    })
    .then(function(r) {
      if (!r.ok) throw new Error('Payment verification failed');
      return r.json();
    })
    .then(function(data) {
      sessionStorage.setItem('pulse_last_order', JSON.stringify(data));
      window.location.href = '/success.html?order=' + encodeURIComponent(ordNum);
    })
    .catch(function(err) {
      console.error(err);
      alert('Payment verification failed. Please try again.');
      if (btn) {
        btn.disabled = false;
        updateSummary();
      }
    });
  }
});
''')
    print('Wrote frontend/js/checkout.js')

    # 5. Success JS
    with open('frontend/js/success.js', 'w', encoding='utf-8') as f:
        f.write('''// PULSE AUDIO - Order Confirmation & Tracking Engine
document.addEventListener('DOMContentLoaded', function() {
  var urlParams = new URLSearchParams(window.location.search);
  var orderNumber = urlParams.get('order');

  if (orderNumber) {
    fetch('/api/orders/' + encodeURIComponent(orderNumber))
      .then(function(res) { return res.json(); })
      .then(function(order) {
        renderOrder(order);

        // Track Meta Pixel Purchase event
        if (window.PulseAnalytics) {
          window.PulseAnalytics.trackEvent('Purchase', {
            content_name: order.item.product_name,
            content_ids: [String(order.item.product_id)],
            content_type: 'product',
            value: order.item.total_amount,
            currency: 'INR',
            order_id: order.order_number,
            num_items: order.item.quantity
          }, order.order_number);
        }
      })
      .catch(function(err) {
        console.error('Order load error:', err);
      });
  }

  function renderOrder(ord) {
    var elId = document.getElementById('orderIdDisplay');
    var elName = document.getElementById('orderCustName');
    var elPh = document.getElementById('orderPhone');
    var elAddr = document.getElementById('orderAddress');
    var elProd = document.getElementById('orderProdName');
    var elAmt = document.getElementById('orderAmount');
    var elVar = document.getElementById('orderVariant');
    var elEst = document.getElementById('orderDeliveryEst');

    if (elId) elId.textContent = ord.order_number;
    if (elName) elName.textContent = ord.customer_name;
    if (elPh) elPh.textContent = '+91 ' + ord.phone;
    if (elAddr) elAddr.textContent = ord.shipping_address.address + ', ' + ord.shipping_address.city + ', ' + ord.shipping_address.state + ' - ' + ord.shipping_address.pincode;
    if (elProd) elProd.textContent = ord.item.product_name;
    if (elAmt) elAmt.textContent = '₹' + ord.item.total_amount.toLocaleString('en-IN');
    if (elVar) elVar.textContent = 'Variant: ' + ord.item.variant + ' (Qty: ' + ord.item.quantity + ')';
    if (elEst) elEst.textContent = ord.delivery_estimate;
  }
});
''')
    print('Wrote frontend/js/success.js')

    # 6. Checkout CSS
    with open('frontend/css/checkout.css', 'w', encoding='utf-8') as f:
        f.write('''/* Checkout & Success Page Styles */
.checkout-header {
  background: #ffffff;
  border-bottom: 1px solid var(--border-light);
  padding: 14px 0;
}

.checkout-header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.checkout-security-tag {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 700;
  color: #047857;
  background: #ecfdf5;
  padding: 4px 10px;
  border-radius: var(--radius-full);
}

.checkout-container {
  padding-top: 24px;
  padding-bottom: 40px;
}

.checkout-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;
}

@media (min-width: 992px) {
  .checkout-grid {
    grid-template-columns: 1.4fr 1fr;
    gap: 32px;
  }
}

.checkout-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 24px;
  box-shadow: var(--shadow-sm);
}

.checkout-card-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--border-light);
}

.step-num {
  width: 28px;
  height: 28px;
  border-radius: var(--radius-full);
  background: var(--color-primary);
  color: #ffffff;
  font-size: 13px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
}

.checkout-card-header h2 {
  font-size: 18px;
  font-weight: 800;
}

.checkout-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr;
  gap: 14px;
}

.form-row.two-col {
  grid-template-columns: 1fr;
}

.form-row.three-col {
  grid-template-columns: 1fr;
}

@media (min-width: 600px) {
  .form-row.two-col { grid-template-columns: 1fr 1fr; }
  .form-row.three-col { grid-template-columns: 1fr 1fr 1.2fr; }
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form-group label {
  font-size: 12px;
  font-weight: 700;
  color: var(--text-muted);
}

.form-group label .req { color: #ef4444; }

.form-group input, .form-group select {
  height: 44px;
  padding: 0 12px;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  font-size: 13px;
  color: var(--text-main);
  background: #f8fafc;
  outline: none;
  transition: var(--transition-fast);
}

.form-group input:focus, .form-group select:focus {
  border-color: var(--color-primary);
  background: #ffffff;
  box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.1);
}

.phone-input-wrap {
  display: flex;
  align-items: center;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  background: #f8fafc;
  overflow: hidden;
}

.phone-input-wrap .country-code {
  padding: 0 12px;
  font-size: 13px;
  font-weight: 800;
  color: var(--text-sub);
  border-right: 1px solid var(--border-light);
  background: #f1f5f9;
}

.phone-input-wrap input {
  border: none;
  background: transparent;
}

.payment-method-selector {
  margin-top: 10px;
}

.selector-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 16px;
  font-weight: 800;
  margin-bottom: 12px;
}

.payment-card-option {
  background: #f5f3ff;
  border: 2px solid var(--color-primary);
  border-radius: var(--radius-md);
  padding: 14px;
}

.option-radio {
  display: flex;
  align-items: center;
  gap: 8px;
}

.option-badge {
  display: inline-block;
  background: #047857;
  color: #ffffff;
  font-size: 10px;
  font-weight: 800;
  padding: 2px 6px;
  border-radius: 4px;
  margin-left: 6px;
}

.payment-sub-logos {
  font-size: 11px;
  color: var(--text-sub);
  margin-top: 6px;
  padding-left: 24px;
}

.btn-proceed-pay {
  width: 100%;
  height: 54px;
  background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%);
  color: #ffffff;
  border: none;
  border-radius: var(--radius-md);
  font-size: 16px;
  font-weight: 900;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4);
  transition: var(--transition-fast);
  margin-top: 10px;
}

.btn-proceed-pay:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(79, 70, 229, 0.5);
}

.btn-proceed-pay:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

/* Order Summary Sticky Card */
.summary-card-sticky {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 24px;
  box-shadow: var(--shadow-sm);
}

@media (min-width: 992px) {
  .summary-card-sticky {
    position: sticky;
    top: 24px;
  }
}

.summary-title {
  font-size: 18px;
  font-weight: 800;
  margin-bottom: 16px;
}

.summary-product-row {
  display: flex;
  gap: 14px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--border-light);
}

.summary-img-box {
  width: 72px;
  height: 72px;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-light);
  background: #f8fafc;
  padding: 4px;
  flex-shrink: 0;
}

.summary-img-box img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.summary-info .prod-name {
  font-size: 14px;
  font-weight: 800;
  line-height: 1.3;
}

.variant-tag {
  font-size: 12px;
  color: var(--text-sub);
  margin: 4px 0;
}

.qty-price-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.qty-badge {
  background: #f1f5f9;
  font-size: 11px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 4px;
}

.price-strong {
  font-size: 14px;
  font-weight: 800;
  color: var(--text-main);
}

.mrp-striked {
  font-size: 12px;
  color: var(--text-light);
  text-decoration: line-through;
}

.applied-coupon-box {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #f5f3ff;
  border: 1px dashed #c4b5fd;
  border-radius: var(--radius-md);
  padding: 10px 14px;
  margin: 16px 0;
}

.applied-coupon-box .coupon-left {
  display: flex;
  align-items: center;
  gap: 8px;
}

.coupon-msg {
  font-size: 11px;
  color: var(--text-sub);
}

.coupon-tag-success {
  background: #047857;
  color: #ffffff;
  font-size: 10px;
  font-weight: 800;
  padding: 2px 6px;
  border-radius: 4px;
}

.price-breakdown {
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-size: 13px;
}

.price-row {
  display: flex;
  justify-content: space-between;
  color: var(--text-muted);
}

.price-divider {
  height: 1px;
  background: var(--border-light);
  margin: 6px 0;
}

.price-row.total-row {
  font-size: 16px;
  color: var(--text-main);
}

.grand-total {
  font-size: 20px;
  font-weight: 900;
  color: var(--color-primary);
}

.summary-trust-perks {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid var(--border-light);
}

.trust-perk {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: var(--text-muted);
  font-weight: 600;
}

/* Success Page Styling */
.success-page {
  background: #f8fafc;
}

.order-placed-pill {
  background: #ecfdf5;
  color: #047857;
  font-size: 12px;
  font-weight: 800;
  padding: 4px 12px;
  border-radius: var(--radius-full);
}

.success-container {
  max-width: 760px;
  padding-top: 30px;
  padding-bottom: 50px;
}

.success-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-xl);
  padding: 36px 24px;
  text-align: center;
  box-shadow: var(--shadow-md);
}

.success-animation-badge {
  width: 64px;
  height: 64px;
  border-radius: var(--radius-full);
  background: #10b981;
  color: #ffffff;
  font-size: 32px;
  font-weight: 900;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 16px;
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
}

.success-title {
  font-family: var(--font-heading);
  font-size: 26px;
  font-weight: 800;
  margin-bottom: 6px;
}

.success-subtitle {
  font-size: 14px;
  color: var(--text-muted);
  margin-bottom: 20px;
}

.order-ref-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #f1f5f9;
  border: 1px solid var(--border-light);
  padding: 8px 18px;
  border-radius: var(--radius-full);
  font-size: 14px;
  margin-bottom: 28px;
}

.tracking-stepper {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 24px 0 32px;
  padding: 0 10px;
}

.step-node {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}

.node-dot {
  width: 32px;
  height: 32px;
  border-radius: var(--radius-full);
  background: #e2e8f0;
  color: #64748b;
  font-size: 13px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
}

.step-node.active .node-dot {
  background: #10b981;
  color: #ffffff;
}

.node-label {
  font-size: 11px;
  font-weight: 700;
  color: var(--text-sub);
}

.step-node.active .node-label {
  color: var(--text-main);
}

.step-connector {
  flex: 1;
  height: 3px;
  background: #e2e8f0;
  margin: 0 6px;
  margin-bottom: 20px;
}

.step-connector.active {
  background: #10b981;
}

.receipt-card-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 14px;
  text-align: left;
  background: #f8fafc;
  border-radius: var(--radius-lg);
  padding: 20px;
  margin-bottom: 24px;
}

@media (min-width: 600px) {
  .receipt-card-grid {
    grid-template-columns: 1fr 1fr;
  }
}

.receipt-section h3 {
  font-size: 12px;
  color: var(--text-sub);
  text-transform: uppercase;
  margin-bottom: 6px;
  letter-spacing: 0.5px;
}

.receipt-section p {
  font-size: 13px;
  color: var(--text-main);
  line-height: 1.4;
}

.warranty-card-box {
  display: flex;
  align-items: center;
  gap: 12px;
  text-align: left;
  background: #ecfdf5;
  border: 1px solid #a7f3d0;
  border-radius: var(--radius-md);
  padding: 14px;
  margin-bottom: 28px;
}

.warranty-card-box .box-icon { font-size: 28px; }
.warranty-card-box h4 { font-size: 13px; font-weight: 800; color: #065f46; }
.warranty-card-box p { font-size: 12px; color: #047857; margin-top: 2px; }

.success-actions-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
}

.btn-continue-shopping {
  padding: 12px 24px;
  background: #0f172a;
  color: #ffffff;
  border-radius: var(--radius-md);
  font-size: 14px;
  font-weight: 800;
  transition: var(--transition-fast);
}

.btn-continue-shopping:hover {
  background: #1e293b;
}

.btn-print-receipt {
  padding: 12px 20px;
  background: #ffffff;
  border: 1px solid var(--border-light);
  color: var(--text-main);
  border-radius: var(--radius-md);
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
}

/* Sandbox Modal Styles */
.sandbox-modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(4px);
  z-index: 99999;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.sandbox-modal-card {
  background: #ffffff;
  border-radius: var(--radius-xl);
  max-width: 440px;
  width: 100%;
  padding: 28px;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.3);
  text-align: center;
}

.sandbox-badge {
  display: inline-block;
  background: #f5f3ff;
  color: var(--color-primary);
  font-size: 10px;
  font-weight: 800;
  padding: 4px 10px;
  border-radius: var(--radius-full);
  margin-bottom: 12px;
}

.sandbox-brand {
  font-size: 18px;
  font-weight: 800;
  color: var(--text-main);
  margin-bottom: 4px;
}

.sandbox-order-no {
  font-size: 12px;
  color: var(--text-sub);
  margin-bottom: 16px;
}

.sandbox-payable-row {
  background: #f8fafc;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 12px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.payable-amt {
  font-size: 20px;
  font-weight: 900;
  color: var(--color-primary);
}

.sandbox-methods {
  display: flex;
  gap: 8px;
  margin-bottom: 18px;
}

.method-chip {
  flex: 1;
  padding: 8px;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  font-size: 11px;
  font-weight: 700;
  color: var(--text-muted);
}

.method-chip.active {
  border-color: var(--color-primary);
  background: #eef2ff;
  color: var(--color-primary);
}

.sandbox-pay-btn {
  width: 100%;
  height: 50px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: #ffffff;
  border: none;
  border-radius: var(--radius-md);
  font-size: 14px;
  font-weight: 900;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);
  margin-bottom: 10px;
}

.sandbox-cancel-btn {
  background: transparent;
  border: none;
  font-size: 12px;
  color: var(--text-sub);
  cursor: pointer;
}
''')
    print('Wrote frontend/css/checkout.css')

if __name__ == '__main__':
    write_files()
    print('All frontend files generated successfully!')

