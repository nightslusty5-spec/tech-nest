import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from backend.app.database import engine, Base
from backend.app.services.seed_data import seed_database
from backend.app.routes import products, checkout, orders

# Initialize DB tables and seed catalogue
try:
    Base.metadata.create_all(bind=engine)
    seed_database()
except Exception as e:
    print(f"Database initialization notice: {e}")

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

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
frontend_dir = os.path.join(BASE_DIR, 'frontend')

if os.path.exists(os.path.join(frontend_dir, 'assets')):
    app.mount('/assets', StaticFiles(directory=os.path.join(frontend_dir, 'assets')), name='assets')
if os.path.exists(os.path.join(frontend_dir, 'css')):
    app.mount('/css', StaticFiles(directory=os.path.join(frontend_dir, 'css')), name='css')
if os.path.exists(os.path.join(frontend_dir, 'js')):
    app.mount('/js', StaticFiles(directory=os.path.join(frontend_dir, 'js')), name='js')

@app.get('/')
def read_index():
    index_file = os.path.join(frontend_dir, 'index.html')
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {'status': 'healthy', 'store': 'PULSE AUDIO'}

@app.get('/product/{slug}')
def read_product_page(slug: str):
    index_file = os.path.join(frontend_dir, 'index.html')
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {'status': 'healthy', 'product': slug}

@app.get('/checkout.html')
@app.get('/checkout')
def read_checkout():
    checkout_file = os.path.join(frontend_dir, 'checkout.html')
    if os.path.exists(checkout_file):
        return FileResponse(checkout_file)
    return {'status': 'checkout'}

@app.get('/success.html')
@app.get('/success')
def read_success():
    success_file = os.path.join(frontend_dir, 'success.html')
    if os.path.exists(success_file):
        return FileResponse(success_file)
    return {'status': 'success'}
