// PULSE AUDIO - Dynamic Checkout & Payment Gateway Engine
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
        if (!r.ok) {
          return r.json().then(function(errData) {
            throw new Error(errData.detail || 'Order creation failed');
          });
        }
        return r.json();
      })
      .then(function(orderData) {
        openRazorpay(orderData);
      })
      .catch(function(err) {
        console.error(err);
        btn.disabled = false;
        updateSummary();
        alert(err.message || 'Unable to initiate checkout. Please try again.');
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
