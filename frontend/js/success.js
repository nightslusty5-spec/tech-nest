// PULSE AUDIO - Order Confirmation & Tracking Engine
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
