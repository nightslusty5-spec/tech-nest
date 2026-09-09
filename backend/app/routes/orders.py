from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.models.order import Order

router = APIRouter(prefix='/orders', tags=['Orders'])

@router.get('/{order_number}')
def get_order_by_number(order_number: str, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.order_number == order_number).first()
    if not order:
        raise HTTPException(status_code=404, detail='Order not found')
    return {
        'order_number': order.order_number,
        'customer_name': order.customer_name,
        'phone': order.phone,
        'email': order.email,
        'shipping_address': {
            'address': order.address,
            'apartment': order.apartment,
            'city': order.city,
            'state': order.state,
            'pincode': order.pincode
        },
        'item': {
            'product_id': order.product_id,
            'product_name': order.product_name,
            'variant': order.variant,
            'quantity': order.quantity,
            'unit_price': order.unit_price,
            'mrp_total': order.mrp_total,
            'discount_amount': order.discount_amount,
            'coupon_code': order.coupon_code,
            'total_amount': order.total_amount
        },
        'payment': {
            'status': order.payment_status,
            'amount': order.total_amount,
            'razorpay_order_id': order.razorpay_order_id,
            'razorpay_payment_id': order.razorpay_payment_id
        },
        'total_amount': order.total_amount,
        'order_status': order.order_status,
        'created_at': order.created_at.strftime('%d %b %Y, %I:%M %p'),
        'delivery_estimate': '3-5 business days'
    }
