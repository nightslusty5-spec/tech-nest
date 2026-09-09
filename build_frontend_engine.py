# Frontend Engine Generator
import os

INDEX_HTML = """<!DOCTYPE html>
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
            <div class="thumbnail-strip hide-mobile" id="desktopThumbnails">
              <!-- Rendered dynamically -->
            </div>

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
            <div class="carousel-dots-row" id="carouselDots">
              <!-- Dots rendered dynamically -->
            </div>
            <div class="mobile-thumbs-scroll" id="mobileThumbsStrip">
              <!-- Mobile Thumbs rendered dynamically -->
            </div>
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
          
          <div class="variant-swatches-grid" id="variantSwatchesGrid">
            <!-- Swatches rendered dynamically -->
          </div>
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
          <ul class="highlights-list" id="highlightsList">
            <!-- Highlights rendered dynamically -->
          </ul>
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
            <div class="accordion-body" id="accBodySpecs">
              <!-- Specs table rendered dynamically -->
            </div>
          </div>

          <!-- Accordion 3: What's in the Box -->
          <div class="accordion-item" data-accordion="box">
            <button class="accordion-header" aria-expanded="false">
              <span class="acc-title">📦 What's In The Box</span>
              <span class="acc-icon">▾</span>
            </button>
            <div class="accordion-body" id="accBodyBox">
              <ul class="box-contents-list" id="boxContentsList">
                <!-- Box contents rendered dynamically -->
              </ul>
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
              <div class="faq-list" id="faqList">
                <!-- FAQs rendered dynamically -->
              </div>
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
      <div class="customer-reviews-grid" id="customerReviewsGrid">
        <!-- Rendered dynamically from DB -->
      </div>
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

  <!-- Dynamic Application Engine -->
  <script src="/js/app.js"></script>
</body>
</html>
"""

# Write index.html
with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(INDEX_HTML)
print('Wrote modern mobile-first frontend/index.html')

# 2. Modern Clean Theme CSS
STYLE_CSS = """/* PULSE AUDIO - Modern High-Converting Light Theme */
:root {
  --font-main: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-heading: 'Space Grotesk', -apple-system, sans-serif;
  
  /* Color Palette */
  --bg-page: #f8fafc;
  --bg-card: #ffffff;
  --bg-card-alt: #f1f5f9;
  
  --text-main: #0f172a;
  --text-muted: #475569;
  --text-sub: #64748b;
  --text-light: #94a3b8;
  
  --color-primary: #4f46e5;
  --color-primary-hover: #4338ca;
  --color-accent: #6366f1;
  --color-cyan: #06b6d4;
  
  --color-green: #10b981;
  --color-green-dark: #047857;
  --color-green-bg: #ecfdf5;
  
  --color-amber: #f59e0b;
  --color-amber-bg: #fffbeb;
  
  --color-red: #ef4444;
  --color-red-bg: #fef2f2;
  
  --border-light: #e2e8f0;
  --border-focus: #6366f1;
  
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 16px -2px rgba(15, 23, 42, 0.08);
  --shadow-lg: 0 10px 30px -4px rgba(15, 23, 42, 0.12);
  
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  --radius-full: 9999px;
  
  --transition-fast: 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-normal: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: var(--font-main);
  background-color: var(--bg-page);
  color: var(--text-main);
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
  -webkit-tap-highlight-color: transparent;
  overflow-x: hidden;
  padding-bottom: 76px; /* Space for mobile sticky bottom CTA */
}

@media (min-width: 992px) {
  body {
    padding-bottom: 0;
  }
}

a {
  color: inherit;
  text-decoration: none;
}

button, input, select {
  font-family: inherit;
  font-size: inherit;
}

.container {
  width: 100%;
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 16px;
}

/* Toast Notifications */
.toast-container {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 99999;
  display: flex;
  flex-direction: column;
  gap: 8px;
  pointer-events: none;
}

.toast-msg {
  background: #0f172a;
  color: #ffffff;
  padding: 12px 20px;
  border-radius: var(--radius-full);
  font-size: 14px;
  font-weight: 700;
  box-shadow: 0 10px 25px rgba(0,0,0,0.25);
  display: flex;
  align-items: center;
  gap: 8px;
  animation: toastIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
  pointer-events: auto;
}

.toast-msg.success {
  background: #064e3b;
  border: 1px solid #10b981;
  color: #ecfdf5;
}

@keyframes toastIn {
  from { opacity: 0; transform: translateY(-16px) scale(0.95); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

/* Top Promo Bar */
.top-announcement-bar {
  background: linear-gradient(90deg, #1e1b4b 0%, #312e81 50%, #1e1b4b 100%);
  color: #e0e7ff;
  font-size: 12px;
  font-weight: 600;
  padding: 7px 0;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

.announcement-inner {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  text-align: center;
}

.announcement-badge {
  background: #f59e0b;
  color: #000;
  font-size: 10px;
  font-weight: 800;
  padding: 2px 8px;
  border-radius: var(--radius-full);
  letter-spacing: 0.5px;
}

.announcement-text code {
  background: rgba(255,255,255,0.15);
  color: #fbbf24;
  padding: 1px 6px;
  border-radius: 4px;
  font-weight: 800;
}

/* Compact Site Header */
.site-header {
  background: #ffffff;
  border-bottom: 1px solid var(--border-light);
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: var(--shadow-sm);
}

.header-inner {
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 6px;
  text-decoration: none;
  flex-shrink: 0;
}

.logo-symbol {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%);
  color: #ffffff;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  font-weight: 900;
  box-shadow: 0 2px 8px rgba(99, 102, 241, 0.35);
}

.logo-text {
  display: flex;
  align-items: baseline;
  gap: 2px;
  font-family: var(--font-heading);
}

.brand-name {
  font-size: 20px;
  font-weight: 800;
  color: #0f172a;
  letter-spacing: -0.5px;
}

.brand-sub {
  font-size: 10px;
  font-weight: 800;
  color: var(--color-primary);
  letter-spacing: 1px;
}

.product-quick-nav {
  flex: 1;
  max-width: 380px;
}

.product-switcher-select {
  width: 100%;
  padding: 6px 10px;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-light);
  background: #f8fafc;
  color: var(--text-main);
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  outline: none;
  transition: var(--transition-fast);
}

.product-switcher-select:focus {
  border-color: var(--color-primary);
  background: #ffffff;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}

.header-trust-tag {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 700;
  color: var(--color-green-dark);
  background: var(--color-green-bg);
  padding: 4px 10px;
  border-radius: var(--radius-full);
}

.cart-action-btn {
  position: relative;
  background: #f1f5f9;
  border: 1px solid var(--border-light);
  width: 38px;
  height: 38px;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition-fast);
}

.cart-action-btn:hover {
  background: #e2e8f0;
}

.cart-icon {
  font-size: 18px;
}

.cart-count-badge {
  position: absolute;
  top: -4px;
  right: -4px;
  background: #ef4444;
  color: #ffffff;
  font-size: 10px;
  font-weight: 800;
  min-width: 18px;
  height: 18px;
  border-radius: 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 4px;
  box-shadow: 0 2px 5px rgba(239, 68, 68, 0.4);
}

/* Breadcrumb */
.breadcrumb-container {
  padding: 10px 0;
  border-bottom: 1px solid var(--border-light);
  background: #ffffff;
}

.breadcrumb-list {
  display: flex;
  align-items: center;
  gap: 8px;
  list-style: none;
  font-size: 12px;
  color: var(--text-sub);
}

.breadcrumb-list a:hover {
  color: var(--color-primary);
  text-decoration: underline;
}

.breadcrumb-list .active {
  color: var(--text-main);
  font-weight: 700;
}
"""

with open('frontend/css/style.css', 'w', encoding='utf-8') as f:
    f.write(STYLE_CSS)
print('Wrote frontend/css/style.css')

# 3. Product Page Component CSS
PRODUCT_CSS = """/* Product Details Page Styles */
.product-main-container {
  padding-top: 16px;
  padding-bottom: 40px;
}

/* Skeleton Loading State */
.skeleton-pulse {
  background: linear-gradient(90deg, #e2e8f0 25%, #f1f5f9 50%, #e2e8f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: var(--radius-md);
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.skeleton-layout {
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;
}

@media (min-width: 992px) {
  .skeleton-layout {
    grid-template-columns: 1fr 1fr;
  }
}

.skeleton-gallery-box {
  width: 100%;
  aspect-ratio: 1/1;
}

.skeleton-info-col {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.skeleton-line {
  height: 24px;
}
.skeleton-line.title { height: 40px; width: 85%; }
.skeleton-line.sub { height: 20px; width: 60%; }
.skeleton-line.price { height: 50px; width: 45%; }
.skeleton-line.btn { height: 56px; width: 100%; margin-top: 20px; }

/* Main Grid Layout */
.product-main-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;
}

@media (min-width: 992px) {
  .product-main-grid {
    grid-template-columns: 520px 1fr;
    gap: 36px;
  }
}

/* Left Gallery Column */
.gallery-sticky-wrapper {
  position: relative;
}

@media (min-width: 992px) {
  .gallery-sticky-wrapper {
    position: sticky;
    top: 76px;
  }
}

.gallery-main-viewport-row {
  display: flex;
  gap: 16px;
}

/* Vertical Thumbnails (Desktop) */
.thumbnail-strip {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 72px;
  flex-shrink: 0;
}

.thumb-btn {
  width: 72px;
  height: 72px;
  border: 2px solid var(--border-light);
  border-radius: var(--radius-md);
  background: #ffffff;
  padding: 4px;
  cursor: pointer;
  transition: var(--transition-fast);
  overflow: hidden;
}

.thumb-btn:hover {
  border-color: var(--color-accent);
}

.thumb-btn.active {
  border-color: var(--color-primary);
  box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.2);
}

.thumb-btn img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

/* Main Image Display */
.main-image-viewer {
  position: relative;
  flex: 1;
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  aspect-ratio: 1/1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  cursor: zoom-in;
}

.bestseller-badge-pill {
  position: absolute;
  top: 14px;
  left: 14px;
  background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
  color: #000000;
  font-size: 11px;
  font-weight: 800;
  padding: 4px 10px;
  border-radius: var(--radius-full);
  z-index: 2;
  box-shadow: 0 2px 6px rgba(245, 158, 11, 0.4);
}

.btn-fullscreen-trigger {
  position: absolute;
  top: 14px;
  right: 14px;
  background: rgba(255,255,255,0.9);
  border: 1px solid var(--border-light);
  width: 34px;
  height: 34px;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 800;
  color: var(--text-main);
  cursor: pointer;
  z-index: 2;
  box-shadow: var(--shadow-sm);
  transition: var(--transition-fast);
}

.btn-fullscreen-trigger:hover {
  background: #ffffff;
  transform: scale(1.08);
}

.main-image-viewer img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  transition: transform 0.25s ease-out;
  transform-origin: center center;
  user-select: none;
  -webkit-user-drag: none;
}

.zoom-hint {
  position: absolute;
  bottom: 12px;
  background: rgba(15, 23, 42, 0.75);
  color: #ffffff;
  font-size: 11px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: var(--radius-full);
  backdrop-filter: blur(4px);
  pointer-events: none;
}

/* Mobile Carousel Controls */
.mobile-gallery-controls {
  margin-top: 12px;
}

.carousel-dots-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  margin-bottom: 10px;
}

.dot-btn {
  width: 8px;
  height: 8px;
  border-radius: 4px;
  background: #cbd5e1;
  border: none;
  padding: 0;
  cursor: pointer;
  transition: var(--transition-fast);
}

.dot-btn.active {
  width: 24px;
  background: var(--color-primary);
}

.mobile-thumbs-scroll {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 6px;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
}

.mobile-thumbs-scroll::-webkit-scrollbar {
  display: none;
}

.mobile-thumb-item {
  width: 58px;
  height: 58px;
  flex-shrink: 0;
  border: 2px solid var(--border-light);
  border-radius: var(--radius-sm);
  background: #ffffff;
  padding: 3px;
}

.mobile-thumb-item.active {
  border-color: var(--color-primary);
}

.mobile-thumb-item img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

/* Desktop CTA Buttons */
.desktop-cta-actions {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 12px;
  margin-top: 20px;
}

.btn-action {
  height: 54px;
  border-radius: var(--radius-md);
  font-size: 15px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  cursor: pointer;
  border: none;
  transition: var(--transition-fast);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.btn-desktop-add-cart {
  background: #ffffff;
  color: var(--color-primary);
  border: 2px solid var(--color-primary);
}

.btn-desktop-add-cart:hover {
  background: #eef2ff;
}

.btn-desktop-buy-now {
  background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%);
  color: #ffffff;
  box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4);
}

.btn-desktop-buy-now:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(79, 70, 229, 0.5);
}

/* Trust Seals Grid */
.trust-seals-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  margin-top: 18px;
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 12px;
}

.seal-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  font-weight: 700;
  color: var(--text-muted);
}

.seal-icon {
  font-size: 15px;
}

/* Right Info Column */
.product-info-column {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.brand-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 6px;
}

.brand-badge-pill {
  background: #e0e7ff;
  color: var(--color-primary);
  font-size: 11px;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: var(--radius-sm);
  letter-spacing: 0.5px;
}

.sku-tag {
  font-size: 12px;
  color: var(--text-sub);
  font-weight: 600;
}

.product-title-heading {
  font-family: var(--font-heading);
  font-size: 22px;
  font-weight: 800;
  color: var(--text-main);
  line-height: 1.3;
}

@media (min-width: 768px) {
  .product-title-heading {
    font-size: 28px;
  }
}

.product-tagline {
  font-size: 13px;
  color: var(--text-muted);
  font-weight: 500;
  margin-top: 4px;
}

/* Ratings & Demand */
.rating-demand-row {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}

.rating-pill-green {
  background: #047857;
  color: #ffffff;
  font-size: 13px;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  gap: 3px;
}

.reviews-count-text {
  font-size: 13px;
  color: var(--text-muted);
  font-weight: 600;
}

.verified-store-tag {
  background: #f1f5f9;
  color: #047857;
  font-size: 11px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: var(--radius-full);
}

/* Stock Status */
.stock-status-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #ecfdf5;
  border: 1px solid #a7f3d0;
  color: #065f46;
  font-size: 12px;
  font-weight: 700;
  padding: 8px 12px;
  border-radius: var(--radius-md);
}

.stock-status-banner.low {
  background: #fffbeb;
  border-color: #fde68a;
  color: #92400e;
}

.stock-status-banner.out {
  background: #fef2f2;
  border-color: #fecaca;
  color: #991b1b;
}

.stock-indicator-dot {
  width: 8px;
  height: 8px;
  border-radius: 4px;
  background: #10b981;
}

.stock-status-banner.low .stock-indicator-dot { background: #f59e0b; }
.stock-status-banner.out .stock-indicator-dot { background: #ef4444; }

/* Price Box */
.price-deal-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 16px;
  box-shadow: var(--shadow-sm);
}

.price-header-row {
  display: flex;
  align-items: baseline;
  gap: 8px;
  flex-wrap: wrap;
}

.price-currency {
  font-size: 20px;
  font-weight: 800;
  color: var(--color-primary);
}

.price-selling {
  font-size: 32px;
  font-weight: 900;
  color: var(--text-main);
  letter-spacing: -1px;
}

.price-mrp {
  font-size: 16px;
  color: var(--text-light);
  text-decoration: line-through;
  font-weight: 600;
}

.price-discount-pill {
  background: #ecfdf5;
  color: #047857;
  font-size: 13px;
  font-weight: 800;
  padding: 3px 10px;
  border-radius: var(--radius-full);
}

.price-sub-info {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: var(--text-sub);
  margin-top: 6px;
  font-weight: 600;
}

.text-green { color: #059669; }

/* Offers Section */
.offers-container {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 16px;
}

.offers-header {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 14px;
  color: var(--text-main);
  margin-bottom: 12px;
}

.offer-cards-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.coupon-item-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  background: #f8fafc;
  border: 1px dashed var(--border-light);
  border-radius: var(--radius-md);
  padding: 12px;
}

.coupon-item-card.highlight {
  background: #f5f3ff;
  border-color: #c4b5fd;
}

.coupon-code-chip {
  display: inline-block;
  background: #4f46e5;
  color: #ffffff;
  font-size: 11px;
  font-weight: 800;
  padding: 2px 8px;
  border-radius: 4px;
  margin-bottom: 4px;
  letter-spacing: 0.5px;
}

.bank-tag-chip {
  display: inline-block;
  background: #0284c7;
  color: #ffffff;
  font-size: 10px;
  font-weight: 800;
  padding: 2px 6px;
  border-radius: 4px;
  margin-bottom: 4px;
}

.coupon-desc {
  font-size: 12px;
  color: var(--text-muted);
  line-height: 1.4;
}

.btn-copy-coupon {
  background: #ffffff;
  border: 1px solid var(--color-primary);
  color: var(--color-primary);
  font-size: 11px;
  font-weight: 800;
  padding: 6px 14px;
  border-radius: var(--radius-full);
  cursor: pointer;
  flex-shrink: 0;
  transition: var(--transition-fast);
}

.btn-copy-coupon:hover {
  background: var(--color-primary);
  color: #ffffff;
}

/* Variant Swatches */
.variants-selection-section {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 16px;
}

.variants-header-row {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  margin-bottom: 12px;
}

.variant-heading {
  color: var(--text-sub);
  font-weight: 600;
}

.selected-variant-label {
  color: var(--text-main);
  font-weight: 700;
}

.variant-swatches-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 10px;
}

.swatch-card {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #f8fafc;
  border: 2px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 8px 10px;
  cursor: pointer;
  text-align: left;
  transition: var(--transition-fast);
}

.swatch-card:hover {
  border-color: var(--color-accent);
}

.swatch-card.active {
  border-color: var(--color-primary);
  background: #eef2ff;
  box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.15);
}

.swatch-thumb {
  width: 36px;
  height: 36px;
  flex-shrink: 0;
  border-radius: var(--radius-sm);
  background: #ffffff;
  padding: 2px;
}

.swatch-thumb img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.swatch-name {
  font-size: 12px;
  font-weight: 700;
  color: var(--text-main);
  line-height: 1.2;
}

.swatch-stock-note {
  font-size: 10px;
  color: #059669;
  font-weight: 600;
}

/* Quantity Stepper */
.quantity-stepper-section {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}

.qty-header-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.qty-heading {
  font-size: 13px;
  font-weight: 700;
  color: var(--text-muted);
}

.qty-stepper-box {
  display: flex;
  align-items: center;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  overflow: hidden;
  background: #f8fafc;
}

.btn-qty-step {
  width: 36px;
  height: 36px;
  background: #ffffff;
  border: none;
  font-size: 16px;
  font-weight: 800;
  color: var(--text-main);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition-fast);
}

.btn-qty-step:hover {
  background: #e2e8f0;
}

.qty-input {
  width: 44px;
  height: 36px;
  border: none;
  background: transparent;
  text-align: center;
  font-size: 14px;
  font-weight: 800;
  color: var(--text-main);
  outline: none;
}

.qty-subtotal-info {
  font-size: 13px;
  color: var(--text-muted);
}

.subtotal-val {
  font-size: 16px;
  font-weight: 800;
  color: var(--color-primary);
  margin-left: 4px;
}

.qty-stock-warning {
  width: 100%;
  font-size: 11px;
  font-weight: 700;
  color: #dc2626;
  margin-top: 4px;
}

/* Pincode Checker */
.pincode-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 16px;
}

.pincode-title-row {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 10px;
}

.pincode-input-group {
  display: flex;
  gap: 8px;
}

.pincode-input-group input {
  flex: 1;
  height: 42px;
  padding: 0 14px;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  font-size: 13px;
  outline: none;
  transition: var(--transition-fast);
}

.pincode-input-group input:focus {
  border-color: var(--color-primary);
  box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.1);
}

.btn-pincode-check {
  background: #0f172a;
  color: #ffffff;
  border: none;
  font-size: 12px;
  font-weight: 800;
  padding: 0 18px;
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: var(--transition-fast);
}

.btn-pincode-check:hover {
  background: #1e293b;
}

.pincode-feedback {
  margin-top: 10px;
  font-size: 12px;
  font-weight: 600;
  padding: 8px 12px;
  border-radius: var(--radius-md);
}

.pincode-feedback.success {
  background: #ecfdf5;
  color: #065f46;
  border: 1px solid #a7f3d0;
}

.pincode-feedback.error {
  background: #fef2f2;
  color: #991b1b;
  border: 1px solid #fecaca;
}

/* Feature Highlights */
.feature-highlights-box {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 16px;
}

.highlights-heading {
  font-size: 14px;
  font-weight: 800;
  margin-bottom: 12px;
}

.highlights-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.highlights-list li {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.4;
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

.highlights-list li::before {
  content: "✓";
  color: #059669;
  font-weight: 800;
}

/* Mobile Accordions */
.accordions-container {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.accordion-item {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  overflow: hidden;
}

.accordion-header {
  width: 100%;
  padding: 14px 16px;
  background: #ffffff;
  border: none;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 14px;
  font-weight: 700;
  color: var(--text-main);
  cursor: pointer;
  text-align: left;
  transition: var(--transition-fast);
}

.accordion-header:hover {
  background: #f8fafc;
}

.acc-icon {
  font-size: 16px;
  color: var(--text-sub);
  transition: transform 0.2s ease;
}

.accordion-body {
  display: none;
  padding: 16px;
  border-top: 1px solid var(--border-light);
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.6;
  background: #fafafa;
}

.accordion-body.active {
  display: block;
}

.accordion-item.open .acc-icon {
  transform: rotate(180deg);
}

/* Specifications Table */
.specs-category-title {
  font-size: 13px;
  font-weight: 800;
  color: var(--color-primary);
  margin-top: 12px;
  margin-bottom: 6px;
}
.specs-category-title:first-child { margin-top: 0; }

.specs-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 6px;
}

.specs-row {
  display: flex;
  justify-content: space-between;
  padding: 6px 8px;
  background: #ffffff;
  border-radius: var(--radius-sm);
  font-size: 12px;
}

.spec-key { color: var(--text-sub); font-weight: 600; }
.spec-val { color: var(--text-main); font-weight: 700; text-align: right; }

/* Box Contents List */
.box-contents-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.box-contents-list li {
  padding: 6px 10px;
  background: #ffffff;
  border-radius: var(--radius-sm);
  font-weight: 600;
}

/* FAQ List */
.faq-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.faq-q {
  font-weight: 800;
  color: var(--text-main);
  margin-bottom: 4px;
}

/* Reviews Section */
.reviews-section {
  margin-top: 40px;
  padding-top: 24px;
  border-top: 1px solid var(--border-light);
}

.reviews-section-header {
  margin-bottom: 20px;
}

.reviews-main-title {
  font-family: var(--font-heading);
  font-size: 22px;
  font-weight: 800;
}

.reviews-sub-title {
  font-size: 13px;
  color: var(--text-sub);
}

.reviews-summary-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 20px;
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
  margin-bottom: 20px;
}

@media (min-width: 768px) {
  .reviews-summary-card {
    grid-template-columns: 240px 1fr;
  }
}

.big-score {
  font-size: 40px;
  font-weight: 900;
  color: var(--text-main);
  line-height: 1;
}

.big-score .star { color: #f59e0b; }

.total-ratings-text {
  font-size: 13px;
  color: var(--text-sub);
  margin: 8px 0;
}

.recommend-tag {
  display: inline-block;
  background: #ecfdf5;
  color: #047857;
  font-size: 11px;
  font-weight: 700;
  padding: 4px 8px;
  border-radius: var(--radius-full);
}

.bars-col {
  display: flex;
  flex-direction: column;
  gap: 6px;
  justify-content: center;
}

.rating-bar-row {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 12px;
  font-weight: 700;
}

.star-label { width: 30px; }
.bar-bg {
  flex: 1;
  height: 8px;
  background: #f1f5f9;
  border-radius: 4px;
  overflow: hidden;
}
.bar-fill {
  height: 100%;
  background: #10b981;
  border-radius: 4px;
}
.pct { width: 32px; text-align: right; color: var(--text-sub); }

/* Review Cards Grid */
.customer-reviews-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

@media (min-width: 768px) {
  .customer-reviews-grid {
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  }
}

.review-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 16px;
}

.review-user-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

.user-avatar {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-full);
  background: #4f46e5;
  color: #ffffff;
  font-size: 13px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
}

.user-name-line {
  font-size: 13px;
  font-weight: 700;
  color: var(--text-main);
}

.user-city-tag {
  font-size: 11px;
  color: #059669;
  font-weight: 600;
}

.review-rating-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 8px;
}

.review-stars { color: #f59e0b; font-size: 13px; }
.review-date { font-size: 11px; color: var(--text-sub); }
.review-var { font-size: 11px; color: var(--color-primary); font-weight: 600; margin-left: auto; }

.review-title {
  font-size: 14px;
  font-weight: 800;
  margin-bottom: 6px;
}

.review-body {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.5;
}

/* Lightbox Modal */
.lightbox-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,0.92);
  z-index: 100000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.btn-lightbox-close {
  position: absolute;
  top: 20px;
  right: 20px;
  background: rgba(255,255,255,0.2);
  border: none;
  color: #ffffff;
  font-size: 24px;
  width: 44px;
  height: 44px;
  border-radius: var(--radius-full);
  cursor: pointer;
}

.lightbox-content {
  max-width: 90vw;
  max-height: 85vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.lightbox-content img {
  max-width: 100%;
  max-height: 75vh;
  object-fit: contain;
}

.lightbox-caption {
  color: #e2e8f0;
  font-size: 14px;
  font-weight: 600;
  margin-top: 14px;
  text-align: center;
}
"""

with open('frontend/css/product.css', 'w', encoding='utf-8') as f:
    f.write(PRODUCT_CSS)
print('Wrote frontend/css/product.css')

# 4. Responsive & Mobile Sticky Bar CSS
RESPONSIVE_CSS = """/* Responsive Breakpoints & Mobile Optimization */
.show-mobile { display: block; }
.hide-mobile { display: none; }

@media (min-width: 768px) {
  .show-mobile { display: none; }
  .hide-mobile { display: block; }
  .hide-mobile.header-trust-tag { display: flex; }
  .hide-mobile.desktop-cta-actions { display: grid; }
}

/* Mobile Sticky Bottom Purchase Bar */
.mobile-sticky-buy-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: #ffffff;
  border-top: 1px solid var(--border-light);
  padding: 10px 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  z-index: 9999;
  box-shadow: 0 -4px 16px rgba(0,0,0,0.08);
}

@media (min-width: 992px) {
  .mobile-sticky-buy-bar {
    display: none;
  }
}

.sticky-price-info {
  display: flex;
  flex-direction: column;
}

.sticky-price-row {
  display: flex;
  align-items: baseline;
  gap: 4px;
}

.sticky-price-row .curr {
  font-size: 14px;
  font-weight: 800;
  color: var(--color-primary);
}

.sticky-price-row .val {
  font-size: 20px;
  font-weight: 900;
  color: var(--text-main);
}

.sticky-price-row .mrp {
  font-size: 12px;
  color: var(--text-light);
  text-decoration: line-through;
}

.shipping-tag {
  font-size: 10px;
  font-weight: 700;
  color: #059669;
}

.sticky-buttons-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.btn-sticky-add-cart {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-md);
  border: 1.5px solid var(--color-primary);
  background: #ffffff;
  color: var(--color-primary);
  font-size: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  flex-shrink: 0;
}

.btn-sticky-buy-now {
  height: 44px;
  padding: 0 20px;
  border-radius: var(--radius-md);
  background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%);
  color: #ffffff;
  font-size: 14px;
  font-weight: 900;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 3px 10px rgba(79, 70, 229, 0.4);
  letter-spacing: 0.5px;
}

.btn-sticky-buy-now:active {
  transform: scale(0.97);
}

/* Footer Styling */
.site-footer {
  background: #0f172a;
  color: #f8fafc;
  padding: 40px 0 20px;
  margin-top: 40px;
}

.footer-inner {
  display: grid;
  grid-template-columns: 1fr;
  gap: 30px;
  margin-bottom: 30px;
}

@media (min-width: 768px) {
  .footer-inner {
    grid-template-columns: 2fr 1fr 1fr;
  }
}

.footer-col-brand .brand-name { color: #ffffff; }
.footer-desc {
  font-size: 13px;
  color: #94a3b8;
  margin: 12px 0 16px;
  line-height: 1.5;
  max-width: 400px;
}

.payment-badges-row {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.badge-chip {
  background: #1e293b;
  color: #cbd5e1;
  font-size: 10px;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 4px;
  border: 1px solid #334155;
}

.footer-col-links h4 {
  font-size: 14px;
  font-weight: 800;
  margin-bottom: 12px;
  color: #ffffff;
}

.footer-col-links ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.footer-col-links a {
  font-size: 13px;
  color: #94a3b8;
  transition: var(--transition-fast);
}

.footer-col-links a:hover {
  color: #ffffff;
}

.footer-bottom-bar {
  border-top: 1px solid #1e293b;
  padding-top: 20px;
  font-size: 12px;
  color: #64748b;
}

.footer-bottom-flex {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  text-align: center;
}

@media (min-width: 768px) {
  .footer-bottom-flex {
    flex-direction: row;
    justify-content: space-between;
  }
}
"""

with open('frontend/css/responsive.css', 'w', encoding='utf-8') as f:
    f.write(RESPONSIVE_CSS)
print('Wrote frontend/css/responsive.css')

# 5. Core Dynamic JavaScript Engine (frontend/js/app.js)
APP_JS = """// PULSE AUDIO - Dynamic Mobile-First Product Engine
document.addEventListener('DOMContentLoaded', function() {
  var state = {
    product: null,
    selectedVariant: null,
    quantity: 1,
    currentImageIndex: 0,
    cartCount: parseInt(localStorage.getItem('pulse_cart_count') || '0', 10)
  };

  updateCartBadge();

  // Determine Product Slug from URL path or parameter
  var urlParams = new URLSearchParams(window.location.search);
  var slugParam = urlParams.get('product');
  var pathSegments = window.location.pathname.split('/').filter(Boolean);
  var pathSlug = (pathSegments[0] === 'product' && pathSegments[1]) ? pathSegments[1] : null;
  var productSlug = slugParam || pathSlug || 'pulse-sonic-pro';

  // Quick Switcher handler
  var switcher = document.getElementById('productQuickSwitcher');
  if (switcher) {
    switcher.value = productSlug;
    switcher.addEventListener('change', function(e) {
      window.location.href = '/?product=' + encodeURIComponent(e.target.value);
    });
  }

  // Load Product Data dynamically
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

        // Track Meta Pixel ViewContent
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
    // SEO & Page Title
    document.title = p.name + ' | Official PULSE AUDIO Store';
    var descEl = document.getElementById('seoMetaDesc');
    if (descEl) descEl.setAttribute('content', p.tagline || p.description.substring(0, 160));

    // Inject JSON-LD Schema
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

    // Breadcrumb
    var bCat = document.getElementById('breadcrumbCategory');
    var bName = document.getElementById('breadcrumbProductName');
    if (bCat) bCat.textContent = p.category;
    if (bName) bName.textContent = p.name;

    // Title & Brand
    document.getElementById('productBrand').textContent = p.brand;
    document.getElementById('productSku').textContent = 'SKU: ' + p.sku;
    document.getElementById('productName').textContent = p.name;
    document.getElementById('productTagline').textContent = p.tagline;
    document.getElementById('productRatingVal').textContent = p.rating;
    document.getElementById('productReviewsCount').textContent = p.review_count.toLocaleString('en-IN') + ' Ratings';

    // Pricing
    updatePricingUI();

    // Stock Status
    updateStockUI();

    // Render Variant Swatches
    renderVariants(p.variants);

    // Render Gallery
    renderGallery(p.gallery_images);

    // Render Highlights
    var hlList = document.getElementById('highlightsList');
    if (hlList) {
      hlList.innerHTML = p.highlights.map(function(h) {
        return '<li>' + escapeHtml(h) + '</li>';
      }).join('');
    }

    // Description Accordion
    var descBody = document.getElementById('productFullDescription');
    if (descBody) descBody.textContent = p.description;

    // Specifications Accordion
    renderSpecifications(p.specifications);

    // Box Contents Accordion
    var boxList = document.getElementById('boxContentsList');
    if (boxList) {
      boxList.innerHTML = p.box_contents.map(function(item) {
        return '<li>✓ ' + escapeHtml(item) + '</li>';
      }).join('');
    }

    // Warranty
    var warEl = document.getElementById('warrantyInfoText');
    if (warEl) warEl.textContent = p.warranty_info;

    // FAQ Accordion
    var faqList = document.getElementById('faqList');
    if (faqList && p.faq) {
      faqList.innerHTML = p.faq.map(function(item) {
        return '<div class="faq-item"><div class="faq-q">Q: ' + escapeHtml(item.q) + '</div><div class="faq-a">' + escapeHtml(item.a) + '</div></div>';
      }).join('');
    }

    // Customer Reviews
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

        // Update active image to variant image
        var mainImg = document.getElementById('mainProductImg');
        if (mainImg && vImg) {
          mainImg.src = vImg;
        }

        updateStockUI();
        showToast('Selected variant: ' + vName.split('(')[0]);
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
            // Swipe Left -> Next
            var nextIdx = (state.currentImageIndex + 1) % images.length;
            switchImage(nextIdx);
          } else {
            // Swipe Right -> Prev
            var prevIdx = (state.currentImageIndex - 1 + images.length) % images.length;
            switchImage(prevIdx);
          }
        }
      }, { passive: true });

      // Desktop Hover Magnifier
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

    // Update thumbs & dots
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
"""

with open('frontend/js/app.js', 'w', encoding='utf-8') as f:
    f.write(APP_JS)
print('Wrote frontend/js/app.js')

print('All frontend code written successfully!')
"""

with open('build_frontend_engine.py', 'w', encoding='utf-8') as f:
    f.write(INDEX_HTML)

