import sys
sys.stdout.reconfigure(encoding='utf-8')
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.database import SessionLocal, engine, Base
from backend.app.services.seed_data import seed_database

# Ensure DB is created and seeded
Base.metadata.create_all(bind=engine)
seed_database()

client = TestClient(app)

print('=== 1. Testing Frontend HTML & Direct Product Routes ===')
r = client.get('/')
assert r.status_code == 200, f'GET / failed: {r.status_code}'
assert 'Pulse Audio' in r.text or 'PULSE' in r.text
print('GET / : SUCCESS (Status 200)')

r = client.get('/product/pulse-sonic-pro')
assert r.status_code == 200, f'GET /product/pulse-sonic-pro failed: {r.status_code}'
print('GET /product/pulse-sonic-pro : SUCCESS (Status 200)')

r = client.get('/product/pulse-hypercharge-33w')
assert r.status_code == 200, f'GET /product/pulse-hypercharge-33w failed: {r.status_code}'
print('GET /product/pulse-hypercharge-33w : SUCCESS (Status 200)')

r = client.get('/checkout.html')
assert r.status_code == 200, f'GET /checkout.html failed: {r.status_code}'
assert 'Delivery Address' in r.text
print('GET /checkout.html : SUCCESS (Status 200)')

r = client.get('/success.html')
assert r.status_code == 200, f'GET /success.html failed: {r.status_code}'
assert 'Thank You For Your Order' in r.text
print('GET /success.html : SUCCESS (Status 200)')


print('\n=== 2. Testing Product API Endpoints ===')
# List all products
r = client.get('/api/products')
assert r.status_code == 200, f'GET /api/products failed: {r.status_code}'
products = r.json()
print(f'Retrieved {len(products)} products from API:')
for p in products:
    print(f" - [{p['slug']}] {p['name']} | Price: INR {p['price']} | Stock: {p.get('stock', 'N/A')}")
assert len(products) >= 4

# Featured product
r = client.get('/api/products/featured')
assert r.status_code == 200
feat = r.json()
print(f'Featured Product: {feat["name"]} (INR {feat["price"]})')
assert feat['price'] == 1.0

# By slug
r = client.get('/api/products/by-slug/pulse-hypercharge-33w')
assert r.status_code == 200
charger = r.json()
assert 'Pulse HyperCharge 33W' in charger['name']
print(f'Get By Slug: {charger["name"]} | INR {charger["price"]}')

# By ID
r = client.get(f'/api/products/{feat["id"]}')
assert r.status_code == 200
assert r.json()['slug'] == feat['slug']
print(f'Get By ID: {feat["id"]} matches slug {feat["slug"]}')


print('\n=== 3. Testing Checkout & Pincode Service ===')
# Pincode check
r = client.post('/api/checkout/check-pincode', json={'pincode': '560038'})
assert r.status_code == 200
pin_res = r.json()
print(f'Pincode 560038 check: {pin_res}')
assert pin_res['serviceable'] == True
assert pin_res['cod_available'] == False, 'COD should be disabled'

# Test COD Order Rejection
cod_test_payload = {
    'product_id': feat['id'],
    'variant_id': 'midnight-obsidian',
    'quantity': 1,
    'payment_method': 'cod',
    'customer_name': 'Test User',
    'phone': '9876543210',
    'email': 'test@example.com',
    'address': 'Test Street',
    'city': 'Bengaluru',
    'state': 'Karnataka',
    'pincode': '560038'
}
r_cod = client.post('/api/checkout/create-order', json=cod_test_payload)
assert r_cod.status_code == 400
assert 'Cash on delivery is not available in your area' in r_cod.json()['detail']
print('COD Order Rejection Test: SUCCESS (400 returned with "Cash on delivery not available in your area")')

# Order creation with online payment (Razorpay / UPI) and coupon
order_payload = {
    'product_id': feat['id'],
    'variant_id': 'midnight-obsidian',
    'quantity': 2,
    'payment_method': 'upi',
    'customer_name': 'Aditya Sharma',
    'phone': '9876543210',
    'email': 'aditya.sharma@example.com',
    'address': 'Flat 402, Sunshine Heights',
    'apartment': 'Indiranagar',
    'city': 'Bengaluru',
    'state': 'Karnataka',
    'pincode': '560038',
    'event_id': 'evt_test_meta_12345'
}
r = client.post('/api/checkout/create-order', json=order_payload)
assert r.status_code == 200, f'Create order failed: {r.text}'
order_res = r.json()
print(f'Order created: {order_res["order_number"]} | Amount: INR {order_res["amount"]}')
# 1.0 * 2 = 2.0
assert order_res['amount'] == 2.0


print('\n=== 4. Testing Paytm Dynamic UPI Auto-Verification & CAPI Trigger ===')
# 1. Test initial pending status
r_stat = client.get(f'/api/checkout/check-order-status/{order_res["order_number"]}')
assert r_stat.status_code == 200
assert r_stat.json()['is_paid'] == False
print(f'Order initial status check: is_paid={r_stat.json()["is_paid"]} (PENDING)')

# 2. Test rejection when user clicks without real bank payment
auto_verify_payload = {
    'order_number': order_res['order_number'],
    'payment_method': 'paytm_upi'
}
r_unpaid = client.post('/api/checkout/auto-verify-payment', json=auto_verify_payload)
assert r_unpaid.status_code == 400
assert 'Payment Not Detected Yet' in r_unpaid.json()['detail']
print('Unpaid Order Rejection Test: SUCCESS (400 returned with "Payment Not Detected Yet")')

# 3. Simulate Paytm Webhook Credit Callback
wh_payload = {
    'ORDERID': order_res['order_number'],
    'STATUS': 'TXN_SUCCESS',
    'TXNID': 'PTM_TXN_' + order_res['order_number']
}
r_wh = client.post('/api/checkout/paytm-webhook', json=wh_payload)
assert r_wh.status_code == 200
print(f'Paytm Webhook Received: {r_wh.json()}')

# 4. Test status polling after credit verification
r_stat_after = client.get(f'/api/checkout/check-order-status/{order_res["order_number"]}')
assert r_stat_after.status_code == 200
assert r_stat_after.json()['is_paid'] == True
print(f'Order status check after webhook credit: is_paid={r_stat_after.json()["is_paid"]} (PAID / CONFIRMED)')


print('\n=== 5. Testing Order Detail Retrieval API ===')
ord_num = order_res['order_number']
r = client.get(f'/api/orders/{ord_num}')
assert r.status_code == 200
fetched = r.json()
print(f'Order details: Name={fetched["customer_name"]}, Status={fetched["order_status"]}, Item={fetched["item"]["product_name"]}, Qty={fetched["item"]["quantity"]}, Total=INR {fetched["payment"]["amount"]}')
assert fetched['item']['quantity'] == 2
assert fetched['payment']['amount'] == 2.0

print('\n' + '='*55)
print('ALL 5 INTEGRATION & END-TO-END TEST SUITES PASSED (100%)!')
print('='*55)
