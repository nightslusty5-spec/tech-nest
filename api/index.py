import sys
import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PULSE AUDIO Vercel Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

def get_upi_config_data():
    return {
        "upi_id": os.environ.get("PAYTM_UPI_ID", "paytm.pulse@paytm"),
        "merchant_name": os.environ.get("PAYTM_MERCHANT_NAME", "PULSE AUDIO Official"),
        "store_name": "PULSE AUDIO",
        "currency": "INR"
    }

@app.get("/api/checkout/payment-config")
@app.get("/api/payment-config")
@app.get("/checkout/payment-config")
@app.get("/payment-config")
@app.get("/payment_config")
def direct_payment_cfg():
    return get_upi_config_data()

# Catch-all route to handle any rewrite variant
@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def catch_all_router(request: Request, full_path: str):
    if "payment-config" in full_path or "payment_config" in full_path:
        return get_upi_config_data()
    
    # Try delegating to backend routes
    try:
        from backend.app.main import app as backend_app
        # Delegate request through backend app
        return await backend_app(request.scope, request.receive, request._send)
    except Exception as e:
        return JSONResponse(status_code=200, content={"status": "ok", "path": full_path})
