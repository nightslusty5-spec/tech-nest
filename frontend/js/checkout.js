// PULSE AUDIO - Dynamic Checkout & Paytm Dynamic QR Gateway Engine
document.addEventListener('DOMContentLoaded', function() {
  var urlParams = new URLSearchParams(window.location.search);
  var sessionItem = JSON.parse(sessionStorage.getItem('pulse_checkout_product') || 'null');

  var checkoutState = sessionItem || {
    productId: 1,
    productSlug: 'pulse-sonic-pro',
    productName: 'Pulse Sonic Pro ANC True Wireless Earbuds',
    variantId: urlParams.get('variant') || 'midnight-obsidian',
    quantity: parseInt(urlParams.get('qty') || '1', 10),
    price: 1.0,
    mrp: 2999.0,
    eventId: 'ic_' + Date.now()
  };

  var appliedCoupon = 'PREPAID100';
  var couponDiscount = 0.0;

  var paymentConfig = {
    upi_id: 'paytm.pulse@paytm',
    merchant_name: 'PULSE AUDIO Official',
    store_name: 'PULSE AUDIO'
  };

  // Fetch dynamic payment config from backend
  function loadPaymentConfig() {
    fetch('/api/checkout/payment-config')
      .then(function(r) {
        if (!r.ok) throw new Error('status ' + r.status);
        return r.json();
      })
      .then(function(cfg) {
        if (cfg && cfg.upi_id) {
          paymentConfig = cfg;
        }
      })
      .catch(function() {
        fetch('/api/payment_config')
          .then(function(r) { return r.json(); })
          .then(function(cfg) {
            if (cfg && cfg.upi_id) {
              paymentConfig = cfg;
            }
          })
          .catch(function() {});
      });
  }
  loadPaymentConfig();

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
    if (elBtn) {
      var isCod = document.getElementById('payCOD') && document.getElementById('payCOD').checked;
      if (isCod) {
        elBtn.innerHTML = '<span>⚠️</span> Pay via UPI / Online (COD Unavailable)';
        elBtn.style.background = 'linear-gradient(135deg, #ef4444 0%, #dc2626 100%)';
      } else {
        elBtn.innerHTML = '<span>🔒</span> PROCEED TO PAYMENT (₹' + finalTotal.toLocaleString('en-IN') + ')';
        elBtn.style.background = 'linear-gradient(135deg, #4f46e5 0%, #6366f1 100%)';
      }
    }
  }

  // Payment Method Selection & COD Restriction Handling
  var optOnlineCard = document.getElementById('optOnlineCard');
  var optCodCard = document.getElementById('optCodCard');
  var payOnlineRadio = document.getElementById('payOnline');
  var payCodRadio = document.getElementById('payCOD');
  var codErrorBanner = document.getElementById('codErrorBanner');
  var codAlertDesc = document.getElementById('codAlertDesc');
  var btnSwitchOnline = document.getElementById('btnSwitchOnline');
  var pinInput = document.getElementById('custPincode');

  function updateCodPincodeText() {
    var curPin = (pinInput && pinInput.value.trim()) ? pinInput.value.trim() : 'your area';
    if (codAlertDesc) {
      codAlertDesc.innerHTML = 'Due to courier logistics restrictions, Cash on Delivery is currently disabled for pincode <strong>' + curPin + '</strong>. Please select <strong>Instant UPI / Online Payment</strong> to complete your order and claim an instant ₹100 discount.';
    }
  }

  function selectOnlinePayment() {
    if (payOnlineRadio) payOnlineRadio.checked = true;
    if (optOnlineCard) optOnlineCard.classList.add('selected');
    if (optCodCard) {
      optCodCard.classList.remove('selected');
      optCodCard.classList.remove('cod-error-active');
    }
    if (codErrorBanner) codErrorBanner.style.display = 'none';
    updateSummary();
  }

  function selectCodPayment() {
    if (payCodRadio) payCodRadio.checked = true;
    if (optOnlineCard) optOnlineCard.classList.remove('selected');
    if (optCodCard) {
      optCodCard.classList.add('selected');
      optCodCard.classList.add('cod-error-active');
    }
    updateCodPincodeText();
    if (codErrorBanner) {
      codErrorBanner.style.display = 'block';
      codErrorBanner.style.animation = 'none';
      void codErrorBanner.offsetHeight; // trigger reflow
      codErrorBanner.style.animation = 'shakeAlert 0.4s ease-in-out';
    }
    updateSummary();
  }

  if (optOnlineCard) {
    optOnlineCard.addEventListener('click', function() {
      selectOnlinePayment();
    });
  }

  if (payOnlineRadio) {
    payOnlineRadio.addEventListener('change', function() {
      selectOnlinePayment();
    });
  }

  if (optCodCard) {
    optCodCard.addEventListener('click', function(e) {
      if (e.target !== btnSwitchOnline) {
        selectCodPayment();
      }
    });
  }

  if (payCodRadio) {
    payCodRadio.addEventListener('change', function() {
      selectCodPayment();
    });
  }

  if (btnSwitchOnline) {
    btnSwitchOnline.addEventListener('click', function(e) {
      e.stopPropagation();
      selectOnlinePayment();
    });
  }

  if (pinInput) {
    pinInput.addEventListener('input', function() {
      if (payCodRadio && payCodRadio.checked) {
        updateCodPincodeText();
      }
    });
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

      // Check if user selected Cash on Delivery
      if (payCodRadio && payCodRadio.checked) {
        selectCodPayment();
        alert('⚠️ Cash on delivery is not available in your area.\n\nPlease select Instant UPI / Online Payment to complete your order and save ₹100.');
        setTimeout(function() {
          selectOnlinePayment();
        }, 800);
        return;
      }

      btn.disabled = true;
      btn.innerHTML = '<span>⏳</span> Initializing Secure Payment Gateway...';

      var payload = {
        product_id: checkoutState.productId,
        variant_id: checkoutState.variantId,
        quantity: checkoutState.quantity,
        coupon_code: appliedCoupon,
        payment_method: 'razorpay',
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
        return r.text().then(function(text) {
          try {
            var data = JSON.parse(text);
            if (!r.ok) {
              throw new Error(data.detail || 'Order creation failed');
            }
            return data;
          } catch(err) {
            if (err.message && err.message.indexOf('Cash on delivery') !== -1) {
              throw err;
            }
            var subtotal = checkoutState.price * checkoutState.quantity;
            var finalTotal = Math.max(1, subtotal - couponDiscount);
            var datePrefix = new Date().toISOString().slice(0,10).replace(/-/g,'');
            var randSuffix = Math.random().toString(36).substring(2, 8).toUpperCase();
            return {
              success: true,
              order_number: 'ORD-' + datePrefix + '-' + randSuffix,
              razorpay_order_id: 'order_pulse_' + Date.now(),
              amount: finalTotal,
              currency: 'INR',
              key_id: 'rzp_test_pulse_sandbox_key',
              customer_name: name,
              phone: phone,
              email: email,
              event_id: checkoutState.eventId,
              is_mock: true
            };
          }
        });
      })
      .then(function(orderData) {
        openPaytmGateway(orderData);
      })
      .catch(function(err) {
        console.error(err);
        btn.disabled = false;
        updateSummary();
        alert(err.message || 'Unable to proceed with payment. Please try again.');
      });
    });
  }

  // Direct 1-Tap UPI Apps & Dynamic QR Gateway with Live UPI ID Customizer
  function openPaytmGateway(orderData) {
    var existingModal = document.getElementById('paytmModal');
    if (existingModal) existingModal.remove();

    var upiId = localStorage.getItem('pulse_custom_upi_id') || paymentConfig.upi_id || 'paytm.pulse@paytm';
    var merchant = paymentConfig.merchant_name || 'PULSE AUDIO Official';
    var amountFormatted = Number(orderData.amount).toFixed(2);
    var orderNum = orderData.order_number;

    function buildUpiLinks(targetUpiId) {
      var baseParams = 'pa=' + encodeURIComponent(targetUpiId) + 
                       '&pn=' + encodeURIComponent(merchant) + 
                       '&am=' + amountFormatted + 
                       '&cu=INR&tn=' + encodeURIComponent('Order_' + orderNum);
      return {
        generic: 'upi://pay?' + baseParams,
        gpay: 'tez://upi/pay?' + baseParams,
        phonepe: 'phonepe://pay?' + baseParams,
        paytm: 'paytmmp://pay?' + baseParams,
        qr: 'https://api.qrserver.com/v1/create-qr-code/?size=240x240&margin=8&data=' + encodeURIComponent('upi://pay?' + baseParams)
      };
    }

    var links = buildUpiLinks(upiId);

    var modal = document.createElement('div');
    modal.id = 'paytmModal';
    modal.className = 'paytm-modal-backdrop';
    modal.innerHTML = `
      <div class="paytm-modal-card" style="position: relative; overflow: hidden;">
        <!-- Header -->
        <div class="paytm-modal-header">
          <div class="paytm-brand-col">
            <span class="paytm-logo-badge">UPI</span>
            <div>
              <div class="paytm-brand-title">Direct 1-Tap UPI Payment</div>
              <small style="opacity: 0.85; font-size: 11px;">Exact Amount Pre-filled • Zero Fees</small>
            </div>
          </div>
          <div class="paytm-timer-pill" id="qrTimerPill">⏱️ 09:59</div>
        </div>

        <!-- Body -->
        <div class="paytm-modal-body">
          <!-- Exact Amount Card -->
          <div class="paytm-amount-card">
            <div class="lbl">Exact Amount to Pay</div>
            <div class="amt">₹${Number(orderData.amount).toLocaleString('en-IN')}</div>
          </div>

          <!-- Section 1: 1-Tap App Payment (Mobile Users) -->
          <div style="margin-bottom: 14px;">
            <div style="font-size: 12px; font-weight: 800; color: #1e293b; margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
              <span>📱</span> <span>Tap Your UPI App to Pay Directly:</span>
            </div>
            <div class="paytm-apps-row">
              <a href="${links.gpay}" class="btn-upi-app" id="btnGPayDirect">
                <span class="app-icon">🟢</span>
                <span>Google Pay</span>
              </a>
              <a href="${links.phonepe}" class="btn-upi-app" id="btnPhonePeDirect">
                <span class="app-icon">🟣</span>
                <span>PhonePe</span>
              </a>
              <a href="${links.paytm}" class="btn-upi-app" id="btnPaytmDirect">
                <span class="app-icon">🔵</span>
                <span>Paytm</span>
              </a>
            </div>
          </div>

          <!-- Section 2: QR Code for Scanner / Desktop -->
          <div class="paytm-qr-container">
            <img src="${links.qr}" id="dynamicQrImgTag" class="paytm-qr-img" alt="Dynamic UPI QR Code">
            <div class="paytm-qr-caption">
              <span>⚡ Or scan QR with any UPI app to pay <strong>₹${Number(orderData.amount).toLocaleString('en-IN')}</strong></span>
            </div>
          </div>

          <!-- UPI ID Copy Box -->
          <div class="paytm-upi-box">
            <div style="flex: 1; text-align: left;">
              <small style="color: #64748b; display: block; font-size: 10px;">RECEIVING UPI ID</small>
              <span class="paytm-upi-val" id="merchantUpiVal">${escapeHtml(upiId)}</span>
            </div>
            <button type="button" class="btn-copy-upi" id="btnCopyUpiId">COPY</button>
          </div>

          <!-- Instant Switch / Test UPI ID Toggle -->
          <div style="margin-top: 10px; text-align: center;">
            <button type="button" id="btnToggleCustomUpi" style="background: transparent; border: none; color: #0284c7; font-size: 11px; font-weight: 700; cursor: pointer; text-decoration: underline;">
              ✏️ Test / Change Receiving UPI ID
            </button>
            <div id="customUpiBox" style="display: none; margin-top: 8px; background: #f8fafc; border: 1px dashed #94a3b8; border-radius: 8px; padding: 10px;">
              <label style="font-size: 11px; font-weight: 700; color: #334155; display: block; margin-bottom: 4px; text-align: left;">Enter any PhonePe / GPay / Paytm UPI ID:</label>
              <div style="display: flex; gap: 6px;">
                <input type="text" id="inputNewUpiId" value="${escapeHtml(upiId)}" placeholder="e.g. 9876543210@okaxis" style="flex: 1; height: 36px; border: 1px solid #cbd5e1; border-radius: 6px; padding: 0 8px; font-size: 12px; font-weight: 700;">
                <button type="button" id="btnApplyNewUpi" style="background: #0284c7; color: #fff; border: none; border-radius: 6px; padding: 0 12px; font-size: 12px; font-weight: 800; cursor: pointer;">APPLY</button>
              </div>
            </div>
          </div>

          <!-- Section 3: Place Order Button -->
          <div style="margin-top: 14px;">
            <button type="button" id="btnIPaid" class="btn-i-paid" style="background: linear-gradient(135deg, #059669 0%, #10b981 100%); font-size: 14px; font-weight: 900; height: 52px;">
              <span>✓</span> I Have Paid ₹${Number(orderData.amount).toLocaleString('en-IN')} — Place Order
            </button>
          </div>
        </div>

        <!-- Footer -->
        <div class="paytm-modal-footer">
          <span class="sec-note">🔒 256-Bit SSL Encrypted</span>
          <button type="button" class="paytm-close-link" id="paytmCloseBtn">Cancel</button>
        </div>
      </div>
    `;
    document.body.appendChild(modal);

    // Live UPI ID Switcher Logic
    var toggleBtn = document.getElementById('btnToggleCustomUpi');
    var customBox = document.getElementById('customUpiBox');
    if (toggleBtn && customBox) {
      toggleBtn.onclick = function() {
        customBox.style.display = customBox.style.display === 'none' ? 'block' : 'none';
      };
    }

    var applyBtn = document.getElementById('btnApplyNewUpi');
    if (applyBtn) {
      applyBtn.onclick = function() {
        var inputVal = document.getElementById('inputNewUpiId').value.trim();
        if (!inputVal || inputVal.indexOf('@') === -1) {
          alert('Please enter a valid UPI ID containing @ (e.g. 9876543210@okaxis or yourname@ybl)');
          return;
        }
        upiId = inputVal;
        localStorage.setItem('pulse_custom_upi_id', inputVal);
        links = buildUpiLinks(inputVal);

        // Update UI
        document.getElementById('merchantUpiVal').textContent = inputVal;
        document.getElementById('dynamicQrImgTag').src = links.qr;
        document.getElementById('btnGPayDirect').href = links.gpay;
        document.getElementById('btnPhonePeDirect').href = links.phonepe;
        document.getElementById('btnPaytmDirect').href = links.paytm;

        customBox.style.display = 'none';
        alert('✓ Updated! Receiving UPI ID is now set to: ' + inputVal);
      };
    }

    // Copy UPI ID button
    document.getElementById('btnCopyUpiId').onclick = function() {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(upiId);
      }
      this.textContent = 'COPIED!';
      var self = this;
      setTimeout(function() { self.textContent = 'COPY'; }, 2000);
    };

    // App Click Handlers
    function setupAppLauncher(btnId, getSchemeFn) {
      var el = document.getElementById(btnId);
      if (!el) return;
      el.addEventListener('click', function(e) {
        e.preventDefault();
        var btnPaid = document.getElementById('btnIPaid');
        if (btnPaid) {
          btnPaid.style.boxShadow = '0 0 0 4px rgba(16, 185, 129, 0.4)';
          btnPaid.innerHTML = '<span>⚡</span> Confirm &amp; Place Order (Payment Done)';
        }
        var scheme = getSchemeFn();
        var now = Date.now();
        window.location.href = scheme;
        setTimeout(function() {
          if (Date.now() - now < 1500) {
            window.location.href = links.generic;
          }
        }, 600);
      });
    }

    setupAppLauncher('btnGPayDirect', function() { return links.gpay; });
    setupAppLauncher('btnPhonePeDirect', function() { return links.phonepe; });
    setupAppLauncher('btnPaytmDirect', function() { return links.paytm; });

    var paymentResolved = false;

    function triggerSuccessCelebration() {
      if (paymentResolved) return;
      paymentResolved = true;
      clearInterval(timerInterval);

      var card = modal.querySelector('.paytm-modal-card');
      if (card) {
        var overlay = document.createElement('div');
        overlay.className = 'paytm-success-overlay';
        overlay.innerHTML = `
          <div class="success-check-circle">✓</div>
          <div class="success-overlay-title">Order Placed Successfully!</div>
          <div class="success-overlay-sub">Payment of ₹${Number(orderData.amount).toLocaleString('en-IN')} Received • Redirecting...</div>
          <div class="success-loader-bar"><div class="success-loader-fill"></div></div>
        `;
        card.appendChild(overlay);
      }

      var name = (document.getElementById('custName') && document.getElementById('custName').value) ? document.getElementById('custName').value : 'Customer';
      var orderInfo = {
        order_number: orderNum,
        customer_name: name,
        order_status: 'CONFIRMED',
        payment: { status: 'PAID', amount: orderData.amount },
        delivery_estimate: '2-3 business days'
      };
      sessionStorage.setItem('pulse_last_order', JSON.stringify(orderInfo));

      setTimeout(function() {
        window.location.href = '/success.html?order=' + encodeURIComponent(orderNum);
      }, 1300);
    }

    // I Have Paid Button handler - places the order
    document.getElementById('btnIPaid').onclick = function() {
      var self = this;
      self.disabled = true;
      self.innerHTML = '<span>⏳</span> Placing Your Order...';
      fetch('/api/checkout/auto-verify-payment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          order_number: orderNum,
          payment_method: 'paytm_upi'
        })
      })
      .then(function(r) { return r.json(); })
      .then(function(res) {
        triggerSuccessCelebration();
      })
      .catch(function() {
        triggerSuccessCelebration();
      });
    };

    // Countdown timer
    var timeLeft = 600;
    var timerInterval = setInterval(function() {
      timeLeft--;
      if (timeLeft <= 0) {
        clearInterval(timerInterval);
        var pill = document.getElementById('qrTimerPill');
        if (pill) pill.textContent = 'Expired';
      } else {
        var mins = Math.floor(timeLeft / 60);
        var secs = timeLeft % 60;
        var pill = document.getElementById('qrTimerPill');
        if (pill) pill.textContent = '⏱️ ' + (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
      }
    }, 1000);

    // Close button
    document.getElementById('paytmCloseBtn').onclick = function() {
      clearInterval(timerInterval);
      modal.remove();
      btn.disabled = false;
      updateSummary();
    };
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
