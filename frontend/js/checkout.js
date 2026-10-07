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

  // Paytm Dynamic UPI QR Gateway Modal with Automatic Detection & Instant Close
  function openPaytmGateway(orderData) {
    var existingModal = document.getElementById('paytmModal');
    if (existingModal) existingModal.remove();

    var upiId = paymentConfig.upi_id || 'paytm.pulse@paytm';
    var merchant = paymentConfig.merchant_name || 'PULSE AUDIO Official';
    var amountFormatted = Number(orderData.amount).toFixed(2);
    var orderNum = orderData.order_number;

    // Official UPI Payment URI Specification
    var upiUri = 'upi://pay?pa=' + encodeURIComponent(upiId) + 
                 '&pn=' + encodeURIComponent(merchant) + 
                 '&am=' + amountFormatted + 
                 '&cu=INR&tn=' + encodeURIComponent('Order_' + orderNum);

    var qrApiUrl = 'https://api.qrserver.com/v1/create-qr-code/?size=240x240&margin=8&data=' + encodeURIComponent(upiUri);

    var modal = document.createElement('div');
    modal.id = 'paytmModal';
    modal.className = 'paytm-modal-backdrop';
    modal.innerHTML = `
      <div class="paytm-modal-card" style="position: relative; overflow: hidden;">
        <!-- Header -->
        <div class="paytm-modal-header">
          <div class="paytm-brand-col">
            <span class="paytm-logo-badge">Paytm</span>
            <div>
              <div class="paytm-brand-title">Dynamic UPI QR Gateway</div>
              <small style="opacity: 0.85; font-size: 11px;">100% Secure &amp; Zero Transaction Fees</small>
            </div>
          </div>
          <div class="paytm-timer-pill" id="qrTimerPill">⏱️ 09:59</div>
        </div>

        <!-- Body -->
        <div class="paytm-modal-body">
          <div class="paytm-amount-card">
            <div class="lbl">Exact Amount Payable</div>
            <div class="amt">₹${Number(orderData.amount).toLocaleString('en-IN')}</div>
          </div>

          <!-- QR Code Box -->
          <div class="paytm-qr-container">
            <img src="${qrApiUrl}" class="paytm-qr-img" alt="Paytm Dynamic UPI QR Code">
            <div class="paytm-qr-caption">
              <span>⚡ Scan with <strong>GPay, PhonePe, Paytm</strong> or Any UPI App</span>
            </div>
          </div>

          <!-- UPI ID Box with Copy Action -->
          <div class="paytm-upi-box">
            <div>
              <small style="color: #64748b; display: block; font-size: 10px;">MERCHANT UPI ID</small>
              <span class="paytm-upi-val" id="merchantUpiVal">${escapeHtml(upiId)}</span>
            </div>
            <button type="button" class="btn-copy-upi" id="btnCopyUpiId">COPY</button>
          </div>

          <!-- Mobile 1-Tap App Links (For Mobile Users) -->
          <div class="paytm-apps-row">
            <a href="${upiUri}" class="btn-upi-app" id="btnAppGpay" target="_blank">
              <span class="app-icon">🟢</span>
              <span>Google Pay</span>
            </a>
            <a href="${upiUri}" class="btn-upi-app" id="btnAppPhonepe" target="_blank">
              <span class="app-icon">🟣</span>
              <span>PhonePe</span>
            </a>
            <a href="${upiUri}" class="btn-upi-app" id="btnAppPaytm" target="_blank">
              <span class="app-icon">🔵</span>
              <span>Paytm UPI</span>
            </a>
          </div>

          <!-- Auto-Detection Radar Box -->
          <div class="paytm-auto-radar">
            <div class="radar-spinner-dot"></div>
            <div class="radar-content">
              <div class="radar-title">⚡ Auto-Detecting Payment (Live)</div>
              <div class="radar-sub">Approve ₹${Number(orderData.amount).toLocaleString('en-IN')} on your UPI App. This screen will automatically confirm and close!</div>
            </div>
          </div>

          <!-- Quick Instant Confirmation Button -->
          <button type="button" id="btnIPaid" class="btn-i-paid">
            <span>✓</span> I Have Paid on My UPI App
          </button>
        </div>

        <!-- Footer -->
        <div class="paytm-modal-footer">
          <span class="sec-note">🔒 256-Bit Bank Grade SSL</span>
          <button type="button" class="paytm-close-link" id="paytmCloseBtn">Cancel</button>
        </div>
      </div>
    `;
    document.body.appendChild(modal);

    // Copy UPI ID button
    document.getElementById('btnCopyUpiId').onclick = function() {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(upiId);
      }
      this.textContent = 'COPIED!';
      var self = this;
      setTimeout(function() { self.textContent = 'COPY'; }, 2000);
    };

    var paymentResolved = false;

    function triggerSuccessCelebration() {
      if (paymentResolved) return;
      paymentResolved = true;
      clearInterval(timerInterval);
      clearInterval(pollInterval);

      var card = modal.querySelector('.paytm-modal-card');
      if (card) {
        var overlay = document.createElement('div');
        overlay.className = 'paytm-success-overlay';
        overlay.innerHTML = `
          <div class="success-check-circle">✓</div>
          <div class="success-overlay-title">Payment Received!</div>
          <div class="success-overlay-sub">₹${Number(orderData.amount).toLocaleString('en-IN')} Received • Confirming Order...</div>
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
      }, 1400);
    }

    // Auto-polling for payment status every 2.5 seconds
    var pollInterval = setInterval(function() {
      if (paymentResolved) return;
      fetch('/api/checkout/check-order-status/' + encodeURIComponent(orderNum))
        .then(function(r) { return r.json(); })
        .then(function(res) {
          if (res && res.is_paid) {
            triggerSuccessCelebration();
          }
        })
        .catch(function() {});
    }, 2500);

    // I Have Paid Button handler
    document.getElementById('btnIPaid').onclick = function() {
      var self = this;
      self.disabled = true;
      self.innerHTML = '<span>⏳</span> Checking Bank Confirmation...';
      fetch('/api/checkout/auto-verify-payment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          order_number: orderNum,
          payment_method: 'paytm_upi'
        })
      })
      .then(function(r) {
        return r.json().then(function(res) {
          if (!r.ok) {
            throw new Error(res.detail || 'Payment not yet detected in your Paytm account.');
          }
          return res;
        });
      })
      .then(function(res) {
        triggerSuccessCelebration();
      })
      .catch(function(err) {
        self.disabled = false;
        self.innerHTML = '<span>⚡</span> Check Payment Status Again';
        alert('⚠️ ' + (err.message || 'Payment not yet detected in the merchant Paytm account. Please approve the payment on Google Pay, PhonePe, or Paytm and try again.'));
      });
    };

    // Clicking intent app link also pre-activates listener
    var appLinks = modal.querySelectorAll('.btn-upi-app');
    appLinks.forEach(function(link) {
      link.addEventListener('click', function() {
        setTimeout(function() {
          var btnPaid = document.getElementById('btnIPaid');
          if (btnPaid) {
            btnPaid.style.background = 'linear-gradient(135deg, #059669 0%, #10b981 100%)';
            btnPaid.innerHTML = '<span>⚡</span> Click Here Once Paid on UPI App';
          }
        }, 1500);
      });
    });

    // Countdown timer
    var timeLeft = 600;
    var timerInterval = setInterval(function() {
      timeLeft--;
      if (timeLeft <= 0) {
        clearInterval(timerInterval);
        clearInterval(pollInterval);
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
      clearInterval(pollInterval);
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
