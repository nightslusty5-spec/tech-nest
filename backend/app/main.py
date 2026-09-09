import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from backend.app.database import engine, Base
from backend.app.services.seed_data import seed_database
from backend.app.routes import products, checkout, orders

Base.metadata.create_all(bind=engine)
seed_database()

app = FastAPI(
    title='PULSE AUDIO E-Commerce Store Engine',
    description='Production-grade mobile-first e-commerce API for Indian electronics consumers with Razorpay and Meta CAPI integration.',
    version='2.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(products.router, prefix='/api')
app.include_router(checkout.router, prefix='/api')
app.include_router(orders.router, prefix='/api')

frontend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'frontend')
app.mount('/assets', StaticFiles(directory=os.path.join(frontend_dir, 'assets')), name='assets')
app.mount('/css', StaticFiles(directory=os.path.join(frontend_dir, 'css')), name='css')
app.mount('/js', StaticFiles(directory=os.path.join(frontend_dir, 'js')), name='js')

@app.get('/')
def read_index():
    return FileResponse(os.path.join(frontend_dir, 'index.html'))

@app.get('/product/{slug}')
def read_product_page(slug: str):
    return FileResponse(os.path.join(frontend_dir, 'index.html'))

@app.get('/checkout.html')
@app.get('/checkout')
def read_checkout():
    return FileResponse(os.path.join(frontend_dir, 'checkout.html'))

@app.get('/success.html')
@app.get('/success')
def read_success():
    return FileResponse(os.path.join(frontend_dir, 'success.html'))
