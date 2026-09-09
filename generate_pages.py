# Page generator script
import os

INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pulse Sonic Pro ANC True Wireless Earbuds | Official PULSE AUDIO Store</title>
  <meta name="description" content="Experience deep bass, crystal clear calls, and 35dB Active Noise Cancellation with the all-new Pulse Sonic Pro TWS Earbuds. 40-hour playtime, 45ms low latency gaming mode.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">
  <link rel="stylesheet" href="/css/product.css">
  <link rel="stylesheet" href="/css/responsive.css">
  <script src="/js/meta-pixel.js"></script>
</head>
<body class="dark-theme">

  <!-- Top Announcement Bar -->
  <div class="top-announcement-bar">
    <div class="container">
      <div class="announcement-content">
        <span class="badge-flash">🔥 LIMITED OFFER</span>
        <span>Flat <strong>₹100 Instant Discount</strong> with coupon <code>PREPAID100</code> | Free Express Delivery across India 🇮🇳</span>
      </div>
    </div>
  </div>

  <!-- Main Store Header -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="brand-logo">
        <div class="logo-symbol">⚡</div>
        <div class="logo-text">
          <span class="brand-name">PULSE</span>
          <span class="brand-sub">AUDIO</span>
        </div>
      </a>

      <div class="header-search-bar">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" placeholder="Search for earbuds, headphones, accessories..." aria-label="Search">
        </div>
      </div>

      <div class="header-actions">
        <div class="header-trust-badge hide-mobile">
          <span class="trust-icon">🛡️</span>
          <div class="trust-info">
            <span class="trust-title">100% Genuine</span>
            <span class="trust-sub">1 Year Warranty</span>
          </div>
        </div>

        <button class="cart-action-btn" id="headerCartBtn" aria-label="View Cart">
          <span class="cart-icon">🛒</span>
          <span class="cart-label hide-mobile">Cart</span>
          <span class="cart-badge">0</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Breadcrumb Navigation -->
  <nav class="breadcrumb-nav" aria-label="Breadcrumb">
    <div class="container">
      <ol class="breadcrumb-list">
        <li><a href="/">Home</a></li>
        <li class="sep">›</li>
        <li><a href="#">Audio &amp; Wearables</a></li>
        <li class="sep">›</li>
        <li><a href="#">TWS Earbuds</a></li>
        <li class="sep">›</li>
        <li class="active" aria-current="page">Pulse Sonic Pro ANC</li>
      </ol>
    </div>
  </nav>

  <!-- Main Product Section -->
  <main class="container product-main-wrapper">
    <div class="product-grid-layout">
      
      <!-- Left Column: Gallery & Purchase Triggers -->
      <div class="product-gallery-column">
        <div class="gallery-sticky-wrapper">
          
          <div class="gallery-viewport-row">
            <!-- Vertical Thumbnails -->
            <div class="thumbnail-column" id="galleryThumbnails">
              <button class="thumb-item active" data-img="/assets/images/earbuds-black.svg" aria-label="View Obsidian Black">
                <img src="/assets/images/earbuds-black.svg" alt="Obsidian Black Earbuds" loading="lazy">
              </button>
              <button class="thumb-item" data-img="/assets/images/earbuds-case.svg" aria-label="View Charging Case">
                <img src="/assets/images/earbuds-case.svg" alt="Charging Case" loading="lazy">
              </button>
              <button class="thumb-item" data-img="/assets/images/earbuds-driver.svg" aria-label="View 13mm Drivers">
                <img src="/assets/images/earbuds-driver.svg" alt="13mm Drivers" loading="lazy">
              </button>
              <button class="thumb-item" data-img="/assets/images/earbuds-anc.svg" aria-label="View 35dB ANC">
                <img src="/assets/images/earbuds-anc.svg" alt="35dB Hybrid ANC" loading="lazy">
              </button>
              <button class="thumb-item" data-img="/assets/images/earbuds-green.svg" aria-label="View Forest Emerald">
                <img src="/assets/images/earbuds-green.svg" alt="Forest Emerald" loading="lazy">
              </button>
              <button class="thumb-item" data-img="/assets/images/earbuds-white.svg" aria-label="View Arctic Ivory">
                <img src="/assets/images/earbuds-white.svg" alt="Arctic Ivory" loading="lazy">
              </button>
            </div>

            <!-- Main Image Viewer -->
            <div class="main-image-card" id="mainImageViewer">
              <div class="bestseller-ribbon">⚡ #1 BESTSELLER IN TWS</div>
              <img id="mainProductImg" src="/assets/images/earbuds-black.svg" alt="Pulse Sonic Pro ANC True Wireless Earbuds">
              <div class="zoom-instruction-hint">
                <span>🔍 Hover to Zoom</span>
              </div>
            </div>
          </div>

          <!-- Desktop Sticky CTA Buttons -->
          <div class="gallery-cta-actions">
            <button class="btn-cta btn-add-to-cart" id="addCartBtn">
              <span class="btn-icon">🛒</span>
              <span>ADD TO CART</span>
            </button>
            <button class="btn-cta btn-buy-now" id="buyNowBtn">
              <span class="btn-icon">⚡</span>
              <span>BUY NOW</span>
            </button>
          </div>

          <!-- Safe Checkout Seals -->
          <div class="trust-badges-row">
            <div class="trust-pill">
              <span class="pill-icon">🔒</span>
              <span>256-Bit SSL Encrypted</span>
            </div>
            <div class="trust-pill">
              <span class="pill-icon">⚡</span>
              <span>Instant Razorpay UPI</span>
            </div>
            <div class="trust-pill">
              <span class="pill-icon">🇮🇳</span>
              <span>Pan-India Delivery</span>
            </div>
          </div>

        </div>
      </div>

      <!-- Right Column: Details, Variant Selector, Pricing, Offers & Specs -->
      <div class="product-info-column">
        
        <!-- Brand & Title Header -->
        <div class="product-header-block">
          <div class="brand-tag-row">
            <span class="brand-pill">PULSE AUDIO OFFICIAL</span>
            <span class="model-no">Model: PA-TW3500</span>
          </div>
          <h1 class="product-title-heading" id="productTitle">
            Pulse Sonic Pro True Wireless Earbuds with 35dB Active Noise Cancellation (ANC)
          </h1>
          <p class="product-subtitle">
            13mm Titanium Drivers | 40-Hour Playtime | Quad Mic ENC Calls | 45ms Ultra-Low Latency Gaming | IPX4 Splash Proof
          </p>
        </div>

        <!-- Rating & Live Social Proof -->
        <div class="ratings-social-block">
          <div class="rating-badge-solid">
            <span class="rating-num">4.8</span>
            <span class="star-icon">★</span>
          </div>
          <span class="rating-count-text">14,820 Ratings &amp; 3,240 Verified Reviews</span>
          <span class="verified-badge-tag">✓ Verified Brand</span>
        </div>

        <div class="live-urgency-banner">
          <div class="pulse-dot"></div>
          <span class="urgency-text"><strong>42 people</strong> are viewing this right now • <strong>Only 14 units</strong> left at this price</span>
        </div>

        <!-- Price & Deal Box -->
        <div class="price-deal-card">
          <div class="price-primary-row">
            <span class="currency-symbol">₹</span>
            <span class="selling-price-val" id="sellingPrice">1,499</span>
            <span class="mrp-val" id="mrpPrice">₹2,999</span>
            <span class="discount-badge-pill" id="discountBadge">50% OFF</span>
          </div>
          <div class="tax-delivery-info">
            <span class="tax-included-text">Inclusive of all taxes</span>
            <span class="dot-sep">•</span>
            <span class="free-ship-text">FREE Express Delivery</span>
          </div>
        </div>

        <!-- Available Offers & Coupons -->
        <div class="available-offers-block">
          <h3 class="section-subhead">
            <span class="subhead-icon">🏷️</span> Available Offers &amp; Coupons
          </h3>
          <div class="offers-list">
            <div class="offer-card highlight-coupon">
              <div class="offer-badge-col">
                <span class="coupon-code-pill">PREPAID100</span>
              </div>
              <div class="offer-details-col">
                <strong>Flat ₹100 Instant Discount</strong> on all prepaid orders (UPI / Cards / Netbanking). Applied automatically at checkout.
              </div>
            </div>

            <div class="offer-card">
              <div class="offer-badge-col">
                <span class="bank-badge">BANK OFFER</span>
              </div>
              <div class="offer-details-col">
                <strong>5% Unlimited Cashback</strong> on HDFC, Axis &amp; ICICI Bank Credit Cards.
              </div>
            </div>

            <div class="offer-card">
              <div class="offer-badge-col">
                <span class="special-badge">SPECIAL</span>
              </div>
              <div class="offer-details-col">
                <strong>Extra ₹1,500 Off</strong> on retail price (Already applied).
              </div>
            </div>
          </div>
        </div>

        <!-- Color / Variant Swatch Selector -->
        <div class="variants-selection-block">
          <div class="variant-header-row">
            <span class="variant-label-title">Color:</span>
            <span class="selected-variant-name" id="selectedVariantName">Midnight Obsidian (Matte Black)</span>
          </div>
          
          <div class="variant-swatches-grid">
            <button class="swatch-card active" data-variant-id="midnight-obsidian" data-variant-name="Midnight Obsidian (Matte Black)" data-img="/assets/images/earbuds-black.svg" aria-label="Select Midnight Obsidian">
              <div class="swatch-thumb">
                <img src="/assets/images/earbuds-black.svg" alt="Midnight Obsidian">
              </div>
              <div class="swatch-info">
                <span class="swatch-title">Obsidian Black</span>
                <span class="swatch-stock-status in-stock">In Stock</span>
              </div>
            </button>

            <button class="swatch-card" data-variant-id="forest-emerald" data-variant-name="Forest Emerald (Deep Green)" data-img="/assets/images/earbuds-green.svg" aria-label="Select Forest Emerald">
              <div class="swatch-thumb">
                <img src="/assets/images/earbuds-green.svg" alt="Forest Emerald">
              </div>
              <div class="swatch-info">
                <span class="swatch-title">Forest Emerald</span>
                <span class="swatch-stock-status in-stock">In Stock</span>
              </div>
            </button>

            <button class="swatch-card" data-variant-id="arctic-ivory" data-variant-name="Arctic Ivory (Ceramic White)" data-img="/assets/images/earbuds-white.svg" aria-label="Select Arctic Ivory">
              <div class="swatch-thumb">
                <img src="/assets/images/earbuds-white.svg" alt="Arctic Ivory">
              </div>
              <div class="swatch-info">
                <span class="swatch-title">Arctic Ivory</span>
                <span class="swatch-stock-status in-stock">In Stock</span>
              </div>
            </button>
          </div>
        </div>

        <!-- Delivery & Pincode Checker -->
        <div class="pincode-checker-card">
          <div class="pincode-header">
            <span class="pin-icon">📍</span>
            <span class="pin-title">Check Delivery Date &amp; COD Availability</span>
          </div>
          <div class="pincode-input-row">
            <input type="text" id="pincodeInput" placeholder="Enter 6-digit PIN code (e.g. 110001, 400001, 560001)" maxlength="6">
            <button class="btn-check-pin" id="checkPinBtn">CHECK</button>
          </div>
          <div id="pincodeResult" class="pincode-result" style="display:none;"></div>
          
          <div class="delivery-perks-list">
            <div class="perk-item">
              <span class="perk-icon">🚀</span>
              <span>Express Delivery in 24-48 Hours</span>
            </div>
            <div class="perk-item">
              <span class="perk-icon">🔄</span>
              <span>7 Days Easy Replacement</span>
            </div>
            <div class="perk-item">
              <span class="perk-icon">🛡️</span>
              <span>1 Year Doorstep Brand Warranty</span>
            </div>
          </div>
        </div>

        <!-- Key Feature Highlights -->
        <div class="product-highlights-block">
          <h3 class="section-subhead">
            <span class="subhead-icon">⭐</span> Key Highlights
          </h3>
          <ul class="highlights-checklist">
            <li><span class="check-bullet">✓</span> <strong>35dB Hybrid Active Noise Cancellation:</strong> Eliminates ambient background rumble, traffic, and office chatter.</li>
            <li><span class="check-bullet">✓</span> <strong>13mm Titanium Dynamic Drivers:</strong> Signature PulseBass™ acoustic tuning for punchy lows and crisp highs.</li>
            <li><span class="check-bullet">✓</span> <strong>40 Hours Combined Playtime:</strong> 8 hours per bud + 32 hours in fast-charging USB Type-C case.</li>
            <li><span class="check-bullet">✓</span> <strong>Quad-Mic Environmental Noise Cancellation (ENC):</strong> Flawless crystal clear calls even in noisy surroundings.</li>
            <li><span class="check-bullet">✓</span> <strong>45ms Beast™ Ultra-Low Latency Mode:</strong> Zero audio lag for competitive BGMI, COD Mobile, and Netflix streaming.</li>
            <li><span class="check-bullet">✓</span> <strong>Bluetooth 5.3 + Insta-Wake N' Pair:</strong> Connects instantly the moment you open the lid.</li>
            <li><span class="check-bullet">✓</span> <strong>IPX4 Sweat &amp; Water Resistance:</strong> Engineered for intense workouts, gym sessions, and monsoon drizzles.</li>
          </ul>
        </div>

        <!-- Technical Specifications Table -->
        <div class="product-specs-section">
          <h3 class="section-subhead">
            <span class="subhead-icon">📋</span> Full Technical Specifications
          </h3>
          
          <div class="specs-category-block">
            <h4 class="specs-cat-title">General</h4>
            <div class="specs-table-grid">
              <div class="spec-row"><span class="spec-label">Model Name</span><span class="spec-value">Pulse Sonic Pro ANC (PA-TW3500)</span></div>
              <div class="spec-row"><span class="spec-label">Color Variants</span><span class="spec-value">Midnight Obsidian, Forest Emerald, Arctic Ivory</span></div>
              <div class="spec-row"><span class="spec-label">Headphone Type</span><span class="spec-value">In the Ear (True Wireless Earbuds)</span></div>
              <div class="spec-row"><span class="spec-label">Inline Remote</span><span class="spec-value">Capacitive Smart Touch Controls</span></div>
              <div class="spec-row"><span class="spec-label">Water Resistance</span><span class="spec-value">IPX4 Splash &amp; Sweat Proof</span></div>
            </div>
          </div>

          <div class="specs-category-block">
            <h4 class="specs-cat-title">Audio &amp; Acoustic Features</h4>
            <div class="specs-table-grid">
              <div class="spec-row"><span class="spec-label">Driver Size</span><span class="spec-value">13mm Titanium Acoustic Drivers</span></div>
              <div class="spec-row"><span class="spec-label">Noise Cancellation</span><span class="spec-value">35dB Hybrid Active Noise Cancellation (ANC) + Transparency Mode</span></div>
              <div class="spec-row"><span class="spec-label">Microphone</span><span class="spec-value">4 x MEMS Microphones with AI-ENC</span></div>
              <div class="spec-row"><span class="spec-label">Frequency Response</span><span class="spec-value">20 Hz - 20,000 Hz</span></div>
              <div class="spec-row"><span class="spec-label">Audio Codecs</span><span class="spec-value">AAC, SBC High-Definition Decoding</span></div>
            </div>
          </div>

          <div class="specs-category-block">
            <h4 class="specs-cat-title">Connectivity &amp; Battery</h4>
            <div class="specs-table-grid">
              <div class="spec-row"><span class="spec-label">Bluetooth Version</span><span class="spec-value">v5.3 + EDR (10m Range)</span></div>
              <div class="spec-row"><span class="spec-label">Gaming Latency</span><span class="spec-value">45ms Ultra-Low Latency Mode</span></div>
              <div class="spec-row"><span class="spec-label">Total Playtime</span><span class="spec-value">Up to 40 Hours (Buds + Case)</span></div>
              <div class="spec-row"><span class="spec-label">Fast Charging</span><span class="spec-value">10 Mins Charge = 120 Mins Playtime</span></div>
              <div class="spec-row"><span class="spec-label">Charging Port</span><span class="spec-value">USB Type-C (Cable Included)</span></div>
            </div>
          </div>

          <div class="specs-category-block">
            <h4 class="specs-cat-title">Warranty &amp; In-The-Box</h4>
            <div class="specs-table-grid">
              <div class="spec-row"><span class="spec-label">Warranty Summary</span><span class="spec-value">1 Year Comprehensive Brand Replacement Warranty</span></div>
              <div class="spec-row"><span class="spec-label">Box Contents</span><span class="spec-value">1 Pair Earbuds, 1 Charging Case, 3 Pairs Silicone Eartips (S/M/L), Type-C Charging Cable, User Manual, Warranty Card</span></div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- Visual Feature Banners Grid -->
    <section class="feature-infographics-section">
      <div class="section-heading-centered">
        <span class="sub-tag">ENGINEERED FOR EXCELLENCE</span>
        <h2>Why Audiophiles Choose Pulse Sonic Pro</h2>
      </div>

      <div class="infographics-grid">
        <div class="info-card">
          <div class="info-img-box">
            <img src="/assets/images/earbuds-anc.svg" alt="35dB Hybrid ANC" loading="lazy">
          </div>
          <h3>35dB Hybrid ANC</h3>
          <p>Dual feed-forward and feedback mics identify external noise before it enters your ear canal, neutralizing up to 98% of ambient noise.</p>
        </div>

        <div class="info-card">
          <div class="info-img-box">
            <img src="/assets/images/earbuds-driver.svg" alt="13mm Titanium Drivers" loading="lazy">
          </div>
          <h3>13mm Titanium Drivers</h3>
          <p>Custom-tuned acoustic diaphragm delivers deep, punchy sub-bass without sacrificing the sparkling treble and warm vocal clarity.</p>
        </div>

        <div class="info-card">
          <div class="info-img-box">
            <img src="/assets/images/earbuds-case.svg" alt="40h Monster Battery" loading="lazy">
          </div>
          <h3>40H Non-Stop Playtime</h3>
          <p>Enjoy up to 8 hours on a single bud charge, and an additional 32 hours stored safely in the compact pocket-friendly Type-C charging case.</p>
        </div>

        <div class="info-card">
          <div class="info-img-box">
            <img src="/assets/images/earbuds-ipx4.svg" alt="IPX4 Sweat Resistance" loading="lazy">
          </div>
          <h3>IPX4 Water &amp; Sweat Proof</h3>
          <p>Precision nano-coating protects internal components against rain, splash, and rigorous workout sweat. Built for your active everyday lifestyle.</p>
        </div>
      </div>
    </section>

    <!-- Customer Reviews & Social Proof Section -->
    <section class="reviews-ratings-section">
      <div class="reviews-header-row">
        <div>
          <h2>Ratings &amp; Customer Reviews</h2>
          <p class="sub-text">100% Verified Purchases from across India</p>
        </div>
        <button class="btn-rate-product">Write a Review</button>
      </div>

      <div class="reviews-score-card">
        <div class="score-summary-col">
          <div class="score-big-num">4.8 <span class="star">★</span></div>
          <p class="score-sub">14,820 Ratings &amp; 3,240 Reviews</p>
          <span class="recommend-pill">⚡ 96% of buyers recommend this product</span>
        </div>

        <div class="rating-bars-col">
          <div class="bar-row"><span class="star-lvl">5 ★</span><div class="bar-track"><div class="bar-fill" style="width:84%;"></div></div><span class="bar-cnt">12,450</span></div>
          <div class="bar-row"><span class="star-lvl">4 ★</span><div class="bar-track"><div class="bar-fill" style="width:11%;"></div></div><span class="bar-cnt">1,630</span></div>
          <div class="bar-row"><span class="star-lvl">3 ★</span><div class="bar-track"><div class="bar-fill" style="width:3%;"></div></div><span class="bar-cnt">445</span></div>
          <div class="bar-row"><span class="star-lvl">2 ★</span><div class="bar-track"><div class="bar-fill" style="width:1%;"></div></div><span class="bar-cnt">150</span></div>
          <div class="bar-row"><span class="star-lvl">1 ★</span><div class="bar-track"><div class="bar-fill" style="width:1%;"></div></div><span class="bar-cnt">145</span></div>
        </div>
      </div>

      <!-- Review Cards List -->
      <div class="reviews-cards-list">
        
        <div class="user-review-card">
          <div class="review-header">
            <div class="user-avatar-chip">AK</div>
            <div class="user-meta">
              <div class="user-name-line">
                <strong>Aditya Kulkarni</strong>
                <span class="verified-check">✓ Verified Buyer (Bengaluru)</span>
              </div>
              <div class="review-stars-date">
                <span class="stars-solid">★★★★★</span>
                <span class="review-date">2 days ago</span>
                <span class="variant-bought">Purchased: Midnight Obsidian</span>
              </div>
            </div>
          </div>
          <h4 class="review-title">Absolute game changer for the price. ANC is remarkably effective!</h4>
          <p class="review-body">I was skeptical about 35dB ANC at under ₹1,500, but these genuinely block out the bus AC and metro drone during my daily commute. Bass is punchy without distorting vocals. Fast charging works as advertised. Highly recommend!</p>
          <div class="review-helpful-row">
            <span class="helpful-count">👍 342 people found this helpful</span>
          </div>
        </div>

        <div class="user-review-card">
          <div class="review-header">
            <div class="user-avatar-chip avatar-purple">PS</div>
            <div class="user-meta">
              <div class="user-name-line">
                <strong>Pooja Sharma</strong>
                <span class="verified-check">✓ Verified Buyer (Delhi NCR)</span>
              </div>
              <div class="review-stars-date">
                <span class="stars-solid">★★★★★</span>
                <span class="review-date">5 days ago</span>
                <span class="variant-bought">Purchased: Forest Emerald</span>
              </div>
            </div>
          </div>
          <h4 class="review-title">Super premium look and incredible mic quality for work calls</h4>
          <p class="review-body">The Forest Emerald finish looks stunning in real life. I use it for daily 4-5 hours of Zoom and Microsoft Teams calls, and my colleagues report zero background ambient disturbance. Fits securely in the ear without causing ear fatigue.</p>
          <div class="review-helpful-row">
            <span class="helpful-count">👍 189 people found this helpful</span>
          </div>
        </div>

        <div class="user-review-card">
          <div class="review-header">
            <div class="user-avatar-chip avatar-amber">RV</div>
            <div class="user-meta">
              <div class="user-name-line">
                <strong>Rahul Verma</strong>
                <span class="verified-check">✓ Verified Buyer (Mumbai)</span>
              </div>
              <div class="review-stars-date">
                <span class="stars-solid">★★★★★</span>
                <span class="review-date">1 week ago</span>
                <span class="variant-bought">Purchased: Arctic Ivory</span>
              </div>
            </div>
          </div>
          <h4 class="review-title">Gaming mode is phenomenal! Zero noticeable latency in BGMI</h4>
          <p class="review-body">Triple-tap toggles Beast Gaming Mode. Gunshots and footsteps are perfectly synced with zero lag. Build quality feels like earbuds costing 3x more. Battery easily lasts 4-5 days of heavy use with the case.</p>
          <div class="review-helpful-row">
            <span class="helpful-count">👍 215 people found this helpful</span>
          </div>
        </div>

      </div>
    </section>

    <!-- FAQ Section -->
    <section class="product-faq-section">
      <div class="section-heading-centered">
        <span class="sub-tag">HAVE QUESTIONS?</span>
        <h2>Frequently Asked Questions</h2>
      </div>

      <div class="faq-accordion">
        <details class="faq-item" open>
          <summary class="faq-question">Does Active Noise Cancellation work on both Android and iOS?</summary>
          <div class="faq-answer">
            <p>Yes! The 35dB Hybrid ANC is hardware-powered directly on the earbuds. It functions seamlessly across all Bluetooth devices including Android phones, iPhones, iPads, MacBooks, and Windows laptops without needing third-party companion software.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">How do I claim the 1-Year Doorstep Warranty?</summary>
          <div class="faq-answer">
            <p>Every Pulse Sonic Pro comes with a 1-Year Comprehensive Replacement Warranty. Simply scan the QR code on the included warranty card or email support@pulse-audio.in with your Order ID for hassle-free doorstep pickup and replacement.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">How does the PREPAID100 discount coupon work?</summary>
          <div class="faq-answer">
            <p>When you proceed to checkout and choose UPI or Online Payment, code PREPAID100 is automatically applied, reducing your total payable price by ₹100 from ₹1,499 down to ₹1,399.</p>
          </div>
        </details>
      </div>
    </section>

  </main>

  <!-- Store Footer -->
  <footer class="site-footer">
    <div class="container footer-inner">
      <div class="footer-brand-col">
        <div class="brand-logo">
          <div class="logo-symbol">⚡</div>
          <div class="logo-text">
            <span class="brand-name">PULSE</span>
            <span class="brand-sub">AUDIO</span>
          </div>
        </div>
        <p class="footer-desc">India's next-generation audio electronics brand. High-fidelity acoustic engineering crafted for uncompromising bass, crystal calls, and all-day endurance.</p>
        <div class="payment-icons-row">
          <span class="pay-badge">UPI</span>
          <span class="pay-badge">GPay</span>
          <span class="pay-badge">PhonePe</span>
          <span class="pay-badge">Paytm</span>
          <span class="pay-badge">Visa</span>
          <span class="pay-badge">Mastercard</span>
          <span class="pay-badge">Razorpay</span>
        </div>
      </div>

      <div class="footer-links-col">
        <h4>Customer Care</h4>
        <ul>
          <li><a href="#">Track Your Order</a></li>
          <li><a href="#">1-Year Warranty Claim</a></li>
          <li><a href="#">7-Day Replacement Policy</a></li>
          <li><a href="#">Shipping &amp; Delivery Terms</a></li>
        </ul>
      </div>

      <div class="footer-links-col">
        <h4>Company</h4>
        <ul>
          <li><a href="#">About Pulse Audio</a></li>
          <li><a href="#">Privacy Policy</a></li>
          <li><a href="#">Terms of Service</a></li>
          <li><a href="#">Contact Support</a></li>
        </ul>
      </div>
    </div>
    
    <div class="footer-bottom-bar">
      <div class="container footer-bottom-inner">
        <p>© 2026 PULSE AUDIO Innovations Pvt Ltd. All Rights Reserved.</p>
        <p class="security-note">🔒 256-Bit SSL Encrypted &amp; Verified Indian E-Commerce Merchant</p>
      </div>
    </div>
  </footer>

  <!-- Mobile Sticky Bottom Buy Bar -->
  <div class="mobile-sticky-buy-bar">
    <div class="sticky-price-col">
      <div class="sticky-price-row">
        <span class="sticky-curr">₹</span>
        <span class="sticky-val">1,499</span>
        <span class="sticky-mrp">₹2,999</span>
      </div>
      <span class="sticky-ship-note">Free Express Shipping</span>
    </div>
    <div class="sticky-btns-col">
      <button class="btn-mobile-buy" id="mobileBuyBtn">
        <span>⚡ BUY NOW</span>
      </button>
    </div>
  </div>

  <script src="/js/app.js"></script>
</body>
</html>
"""

CHECKOUT_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Secure Checkout | PULSE AUDIO Official Store</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">
  <link rel="stylesheet" href="/css/checkout.css">
  <link rel="stylesheet" href="/css/responsive.css">
  <script src="/js/meta-pixel.js"></script>
  <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
</head>
<body class="dark-theme checkout-page">

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
        <span>100% Safe &amp; Secure 256-Bit Checkout</span>
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
                <input type="text" id="custName" placeholder="e.g. Rahul Sharma" required value="Aditya Sharma">
              </div>
            </div>

            <div class="form-row two-col">
              <div class="form-group">
                <label for="custPhone">Mobile Number (for tracking &amp; OTP) <span class="req">*</span></label>
                <div class="phone-input-wrap">
                  <span class="country-code">+91</span>
                  <input type="tel" id="custPhone" placeholder="9876543210" maxlength="10" required value="9876543210">
                </div>
              </div>

              <div class="form-group">
                <label for="custEmail">Email Address (for invoice &amp; receipt) <span class="req">*</span></label>
                <input type="email" id="custEmail" placeholder="rahul.sharma@example.com" required value="aditya.sharma@gmail.com">
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
                <span class="step-num">2</span> Select Payment Option
              </h3>
              
              <div class="payment-card-option selected">
                <div class="option-radio">
                  <input type="radio" id="payOnline" name="paymentMethod" value="razorpay" checked>
                  <label for="payOnline">
                    <strong>Razorpay Instant UPI / Cards / NetBanking</strong>
                    <span class="option-badge">Instant ₹100 Discount Applied</span>
                  </label>
                </div>
                <div class="payment-sub-logos">
                  <span>⚡ GPay, PhonePe, Paytm, BHIM UPI, All Major Credit/Debit Cards</span>
                </div>
              </div>
            </div>

            <div class="submit-action-row">
              <button type="submit" class="btn-proceed-pay" id="proceedPayBtn">
                <span>🔒</span> PROCEED TO PAYMENT (₹1,399)
              </button>
            </div>
          </form>
        </div>
      </div>

      <!-- Right Column: Order Summary & Coupon Breakdown -->
      <div class="checkout-summary-column">
        <div class="summary-card-sticky">
          <h3 class="summary-title">Order Summary</h3>

          <div class="summary-product-row">
            <div class="summary-img-box">
              <img src="/assets/images/earbuds-black.svg" alt="Pulse Sonic Pro ANC">
            </div>
            <div class="summary-info">
              <h4 class="prod-name">Pulse Sonic Pro ANC True Wireless Earbuds</h4>
              <p class="variant-tag" id="summaryVariantName">Variant: Midnight Obsidian</p>
              <div class="qty-price-row">
                <span class="qty-badge">Qty: 1</span>
                <span class="price-strong">₹1,499</span>
                <span class="mrp-striked">₹2,999</span>
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
              <span class="strike">₹2,999</span>
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
              <span>7 Days No-Questions Replacement</span>
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
"""

SUCCESS_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Order Confirmed | PULSE AUDIO</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">
  <link rel="stylesheet" href="/css/checkout.css">
  <link rel="stylesheet" href="/css/responsive.css">
  <script src="/js/meta-pixel.js"></script>
</head>
<body class="dark-theme success-page">

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
          <span class="node-label">Payment Received</span>
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
          <p><strong>Pulse Sonic Pro ANC Earbuds</strong></p>
          <p id="orderVariant">Variant: Midnight Obsidian</p>
        </div>

        <div class="receipt-section">
          <h3>Payment &amp; Delivery</h3>
          <p>Amount Paid: <strong class="text-green" id="orderAmount">₹1,399</strong></p>
          <p>Est. Delivery: <strong id="orderDeliveryEst">Tomorrow by 8 PM</strong></p>
        </div>
      </div>

      <div class="warranty-card-box">
        <span class="box-icon">🛡️</span>
        <div>
          <h4>1-Year Official Doorstep Warranty Activated</h4>
          <p>Your electronic warranty card and GST invoice have been sent to your registered email address.</p>
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
"""

CHECKOUT_JS = """// PULSE AUDIO - Checkout & Razorpay Integration
document.addEventListener('DOMContentLoaded', function() {
  var checkoutState = JSON.parse(sessionStorage.getItem('pulse_checkout_product')) || {
    productId: 1,
    productName: 'Pulse Sonic Pro ANC Earbuds',
    variantId: 'midnight-obsidian',
    quantity: 1,
    price: 1499.0,
    mrp: 2999.0,
    eventId: 'evt_' + Date.now()
  };

  var appliedCoupon = 'PREPAID100';
  var couponDiscount = 100.0;
  updateSummary();

  // Track InitiateCheckout via Meta Pixel
  if (window.PulseAnalytics) {
    window.PulseAnalytics.trackEvent('InitiateCheckout', {
      content_name: checkoutState.productName,
      content_ids: [String(checkoutState.productId)],
      content_type: 'product',
      value: checkoutState.price,
      currency: 'INR',
      num_items: checkoutState.quantity
    }, checkoutState.eventId);
  }

  function updateSummary() {
    var subtotal = checkoutState.price * checkoutState.quantity;
    var finalTotal = Math.max(1, subtotal - couponDiscount);
    var elSub = document.getElementById('summarySubtotal');
    var elDisc = document.getElementById('summaryDiscount');
    var elTotal = document.getElementById('summaryTotal');
    var elBtn = document.getElementById('proceedPayBtn');
    var elVar = document.getElementById('summaryVariantName');
    
    if (elSub) elSub.textContent = '₹' + subtotal.toLocaleString('en-IN');
    if (elDisc) elDisc.textContent = '-₹' + couponDiscount.toLocaleString('en-IN');
    if (elTotal) elTotal.textContent = '₹' + finalTotal.toLocaleString('en-IN');
    if (elBtn) elBtn.innerHTML = '<span class="lock-icon">🔒</span> PROCEED TO PAYMENT (₹' + finalTotal.toLocaleString('en-IN') + ')';
    if (elVar) {
      var names = {
        'midnight-obsidian': 'Midnight Obsidian (Matte Black)',
        'forest-emerald': 'Forest Emerald (Deep Green)',
        'arctic-ivory': 'Arctic Ivory (Ceramic White)'
      };
      elVar.textContent = 'Variant: ' + (names[checkoutState.variantId] || checkoutState.variantId);
    }
  }

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
      btn.innerHTML = '<span class="spinner"></span> Initializing Secure Payment Gateway...';

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
        alert('Unable to initiate checkout session. Please try again.');
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
        description: 'Pulse Sonic Pro ANC True Wireless Earbuds',
        order_id: orderData.razorpay_order_id,
        prefill: {
          name: orderData.customer_name,
          email: orderData.email,
          contact: orderData.phone
        },
        theme: {
          color: '#00d2ff'
        },
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
        <div class="sandbox-badge">RAZORPAY SECURE GATEWAY (SANDBOX)</div>
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
      alert('Payment verification failed. Please check with customer support.');
      if (btn) {
        btn.disabled = false;
        updateSummary();
      }
    });
  }
});
"""

# Write files
with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(INDEX_HTML)
print('Wrote frontend/index.html')

with open('frontend/checkout.html', 'w', encoding='utf-8') as f:
    f.write(CHECKOUT_HTML)
print('Wrote frontend/checkout.html')

with open('frontend/success.html', 'w', encoding='utf-8') as f:
    f.write(SUCCESS_HTML)
print('Wrote frontend/success.html')

with open('frontend/js/checkout.js', 'w', encoding='utf-8') as f:
    f.write(CHECKOUT_JS)
print('Wrote frontend/js/checkout.js')

print('All pages written successfully!')

