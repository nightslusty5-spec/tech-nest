from pydantic import BaseModel, Field
from typing import Optional

class PincodeCheckRequest(BaseModel):
    pincode: str = Field(..., min_length=6, max_length=6)

class PincodeCheckResponse(BaseModel):
    pincode: str
    serviceable: bool
    city: str
    state: str
    estimated_days: str
    free_delivery: bool
    cod_available: bool
    message: str

class CouponCheckRequest(BaseModel):
    code: str
    product_id: int

class CouponCheckResponse(BaseModel):
    valid: bool
    code: str
    discount_amount: float
    message: str

class CreateOrderRequest(BaseModel):
    product_id: int
    variant_id: str
    quantity: int = 1
    coupon_code: Optional[str] = None
    customer_name: str
    phone: str
    email: str
    address: str
    apartment: Optional[str] = ''
    city: str
    state: str
    pincode: str
    payment_method: Optional[str] = 'razorpay'
    event_id: Optional[str] = None

class CreateOrderResponse(BaseModel):
    success: bool
    order_number: str
    razorpay_order_id: str
    amount: float
    currency: str = 'INR'
    key_id: str
    customer_name: str
    phone: str
    email: str
    event_id: str
    is_mock: bool

class VerifyPaymentRequest(BaseModel):
    order_number: str
    razorpay_order_id: str
    razorpay_payment_id: str
    razorpay_signature: str

class VerifyPaymentResponse(BaseModel):
    success: bool
    message: str
    order_number: str
    order_status: str
    amount_paid: float
    product_name: str
    variant: str
    delivery_estimate: str
