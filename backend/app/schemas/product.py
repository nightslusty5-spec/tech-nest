from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class VariantSchema(BaseModel):
    id: str
    name: str
    color_code: str
    badge: Optional[str] = None
    image: str
    stock: int
    in_stock: bool

class ProductResponse(BaseModel):
    id: int
    slug: str
    sku: Optional[str] = 'PA-PRO-001'
    name: str
    tagline: Optional[str] = None
    brand: str
    category: str
    mrp: float
    price: float
    discount_percent: int
    stock: int = 25
    rating: float
    review_count: int
    description: str
    highlights: List[str]
    specifications: Dict[str, Any]
    box_contents: List[str]
    warranty_info: str
    variants: List[VariantSchema]
    gallery_images: List[Dict[str, str]]
    faq: Optional[List[Dict[str, str]]] = []
    reviews: Optional[List[Dict[str, Any]]] = []
    is_active: bool

    class Config:
        from_attributes = True

