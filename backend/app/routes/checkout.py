from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import uuid
import re
from backend.app.database import get_db
from backend.app.models.product import Product
from backend.app.models.order import Order
from backend.app.schemas.order import (
    PincodeCheckRequest, PincodeCheckResponse,
    CouponCheckRequest, CouponCheckResponse,
    CreateOrderRequest, CreateOrderResponse,
    VerifyPaymentRequest, VerifyPaymentResponse
)
from backend.app.services.seed_data import PINCODE_DATA
from backend.app.services.razorpay_service import razorpay_service
from backend.app.services.meta_capi_service import meta_capi

router = APIRouter(prefix='/checkout', tags=['Checkout'])

@router.post('/check-pincode', response_model=PincodeCheckResponse)
def check_delivery_pincode(req: PincodeCheckRequest):
    pin = req.pincode.strip()
    if not re.match(r'^[1-9][0-9]{5}$', pin):
        return PincodeCheckResponse(
            pincode=pin,
            serviceable=False,
            city='',
            state='',
            estimated_days='',
            free_delivery=False,
            cod_available=False,
            message='Invalid PIN code. Please enter a valid 6-digit Indian PIN code.'
        )
    if pin in PINCODE_DATA:
        info = PINCODE_DATA[pin]
        city = info['city']
        state = info['state']
        days = info['days']
        return PincodeCheckResponse(
            pincode=pin,
            serviceable=True,
            city=city,
            state=state,
            estimated_days=days,
            free_delivery=True,
            cod_available=False,
            message=f'✓ Express Delivery Available to {city}, {state} (Expected {days}) • Online Payment Only'
        )
    return PincodeCheckResponse(
        pincode=pin,
        serviceable=True,
        city='Express Hub',
        state='India',
        estimated_days='3-5 business days',
        free_delivery=True,
        cod_available=False,
        message='✓ Express Delivery Available via BlueDart / Delhivery (Expected 3-5 days) • Online Payment Only'
    )

@router.post('/apply-coupon', response_model=CouponCheckResponse)
def check_coupon(req: CouponCheckRequest, db: Session = Depends(get_db)):
    code = req.code.strip().upper()
    product = db.query(Product).filter(Product.id == req.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    if code == 'PREPAID100':
        return CouponCheckResponse(valid=True, code='PREPAID100', discount_amount=100.0, message='Special ₹100 Instant Discount Applied on Prepaid Orders!')
    elif code == 'PULSE50':
        return CouponCheckResponse(valid=True, code='PULSE50', discount_amount=50.0, message='₹50 Pulse Audio First Order Discount Applied!')
    return CouponCheckResponse(valid=False, code=code, discount_amount=0.0, message='Invalid or expired coupon code. Use PREPAID100 for ₹100 instant off.')

@router.post('/create-order', response_model=CreateOrderResponse)
def create_checkout_order(req: CreateOrderRequest, db: Session = Depends(get_db)):
    if req.payment_method and req.payment_method.strip().lower() == 'cod':
        raise HTTPException(
            status_code=400,
            detail='Cash on delivery is not available in your area. Please pay online via UPI, Cards, or NetBanking.'
        )
    product = db.query(Product).filter(Product.id == req.product_id, Product.is_active == True).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found or currently unavailable')
    chosen_variant = None
    for v in product.variants:
        if v.get('id') == req.variant_id:
            chosen_variant = v
            break
    if not chosen_variant:
        raise HTTPException(status_code=400, detail='Selected color variant does not exist')
    if not chosen_variant.get('in_stock') or chosen_variant.get('stock', 0) < req.quantity:
        raise HTTPException(status_code=400, detail='Selected variant is currently out of stock')
    if req.quantity < 1 or req.quantity > 5:
        raise HTTPException(status_code=400, detail='Quantity must be between 1 and 5 per order')
    unit_price = float(product.price)
    mrp_total = float(product.mrp) * req.quantity
    subtotal = unit_price * req.quantity
    shipping_fee = 0.0
    discount = 0.0
    coupon = (req.coupon_code or '').strip().upper()
    if coupon == 'PREPAID100':
        discount = 100.0
    elif coupon == 'PULSE50':
        discount = 50.0
    total_amount = max(1.0, subtotal - discount + shipping_fee)
    date_prefix = datetime.utcnow().strftime('%Y%m%d')
    unique_suffix = uuid.uuid4().hex[:6].upper()
    order_number = f'ORD-{date_prefix}-{unique_suffix}'
    event_id = req.event_id or f'evt_{uuid.uuid4().hex}'
    rzp_res = razorpay_service.create_order(amount_in_rupees=total_amount, order_number=order_number, receipt=order_number)
    new_order = Order(
        order_number=order_number,
        customer_name=req.customer_name.strip(),
        phone=req.phone.strip(),
        email=req.email.strip(),
        address=req.address.strip(),
        apartment=(req.apartment or '').strip(),
        city=req.city.strip(),
        state=req.state.strip(),
        pincode=req.pincode.strip(),
        product_id=product.id,
        product_name=product.name,
        variant=chosen_variant.get('name', req.variant_id),
        quantity=req.quantity,
        unit_price=unit_price,
        mrp_total=mrp_total,
        shipping_fee=shipping_fee,
        discount_amount=discount,
        coupon_code=coupon if discount > 0 else None,
        total_amount=total_amount,
        razorpay_order_id=rzp_res['razorpay_order_id'],
        event_id=event_id,
        payment_status='PENDING_PAYMENT',
        order_status='PROCESSING'
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    meta_capi.send_event(
        event_name='InitiateCheckout',
        event_id=f'ic_{event_id}',
        user_data={'email': req.email, 'phone': req.phone, 'first_name': req.customer_name.split()[0] if req.customer_name else '', 'city': req.city, 'state': req.state, 'pincode': req.pincode},
        custom_data={'currency': 'INR', 'value': total_amount, 'num_items': req.quantity, 'content_name': product.name, 'content_category': product.category, 'content_ids': [str(product.id)]}
    )
    return CreateOrderResponse(
        success=True,
        order_number=order_number,
        razorpay_order_id=rzp_res['razorpay_order_id'],
        amount=total_amount,
        currency='INR',
        key_id=razorpay_service.key_id,
        customer_name=req.customer_name,
        phone=req.phone,
        email=req.email,
        event_id=event_id,
        is_mock=rzp_res['is_mock']
    )

@router.post('/verify-payment', response_model=VerifyPaymentResponse)
def verify_payment(req: VerifyPaymentRequest, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.order_number == req.order_number).first()
    if not order:
        raise HTTPException(status_code=404, detail='Order not found')
    if order.payment_status == 'PAID':
        return VerifyPaymentResponse(
            success=True,
            message='Payment already verified and confirmed.',
            order_number=order.order_number,
            order_status=order.order_status,
            amount_paid=order.total_amount,
            product_name=order.product_name,
            variant=order.variant,
            delivery_estimate='3-5 business days'
        )
    is_valid = razorpay_service.verify_payment_signature(
        razorpay_order_id=req.razorpay_order_id,
        razorpay_payment_id=req.razorpay_payment_id,
        razorpay_signature=req.razorpay_signature
    )
    if not is_valid:
        order.payment_status = 'FAILED'
        db.commit()
        raise HTTPException(status_code=400, detail='Razorpay signature verification failed. Untrusted payment payload.')
    order.payment_status = 'PAID'
    order.order_status = 'CONFIRMED'
    order.razorpay_payment_id = req.razorpay_payment_id
    order.razorpay_signature = req.razorpay_signature
    db.commit()
    meta_capi.send_event(
        event_name='Purchase',
        event_id=order.event_id or f'pur_{order.order_number}',
        user_data={'email': order.email, 'phone': order.phone, 'first_name': order.customer_name.split()[0] if order.customer_name else '', 'city': order.city, 'state': order.state, 'pincode': order.pincode},
        custom_data={'currency': 'INR', 'value': order.total_amount, 'order_id': order.order_number, 'content_name': order.product_name, 'num_items': order.quantity, 'content_ids': [str(order.product_id)]}
    )
    return VerifyPaymentResponse(
        success=True,
        message='Payment verified successfully. Order confirmed!',
        order_number=order.order_number,
        order_status=order.order_status,
        amount_paid=order.total_amount,
        product_name=order.product_name,
        variant=order.variant,
        delivery_estimate='3-5 business days'
    )
