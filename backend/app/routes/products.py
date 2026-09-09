from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.app.database import get_db
from backend.app.models.product import Product
from backend.app.schemas.product import ProductResponse

router = APIRouter(prefix='/products', tags=['Products'])

@router.get('', response_model=List[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.is_active == True).all()

@router.get('/featured', response_model=ProductResponse)
def get_featured_product(db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.is_active == True).first()
    if not product:
        raise HTTPException(status_code=404, detail='No active products found')
    return product

@router.get('/by-slug/{slug}', response_model=ProductResponse)
def get_product_by_slug(slug: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.slug == slug, Product.is_active == True).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    return product

@router.get('/{identifier}', response_model=ProductResponse)
def get_product_by_id_or_slug(identifier: str, db: Session = Depends(get_db)):
    if identifier.isdigit():
        product = db.query(Product).filter(Product.id == int(identifier), Product.is_active == True).first()
    else:
        product = db.query(Product).filter(Product.slug == identifier, Product.is_active == True).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    return product

