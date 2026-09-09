from sqlalchemy import Column, Integer, String, Text, Float, Boolean, JSON
from backend.app.database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(100), unique=True, index=True)
    sku = Column(String(50), default='PA-PRO-001')
    name = Column(String(255), nullable=False)
    tagline = Column(String(255), nullable=True)
    brand = Column(String(100), default='PULSE AUDIO')
    category = Column(String(100), default='Audio & Wearables')
    mrp = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    discount_percent = Column(Integer, nullable=False)
    stock = Column(Integer, default=25)
    rating = Column(Float, default=4.8)
    review_count = Column(Integer, default=1420)
    description = Column(Text, nullable=False)
    highlights = Column(JSON, default=list)
    specifications = Column(JSON, default=dict)
    box_contents = Column(JSON, default=list)
    warranty_info = Column(String(255), default='1 Year Manufacturer Replacement Warranty')
    variants = Column(JSON, default=list)
    gallery_images = Column(JSON, default=list)
    faq = Column(JSON, default=list)
    reviews = Column(JSON, default=list)
    is_active = Column(Boolean, default=True)

