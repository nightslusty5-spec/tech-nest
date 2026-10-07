import sys
import os
import json
import traceback

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

try:
    from backend.app.main import app
except Exception as e:
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    from fastapi.middleware.cors import CORSMiddleware
    
    app = FastAPI(title="PULSE AUDIO Fallback Engine")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
    err_tb = traceback.format_exc()
    
    @app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
    def catch_all_fallback(full_path: str):
        if "payment-config" in full_path:
            return {
                "upi_id": os.environ.get("PAYTM_UPI_ID", "paytm.pulse@paytm"),
                "merchant_name": os.environ.get("PAYTM_MERCHANT_NAME", "PULSE AUDIO Official"),
                "store_name": "PULSE AUDIO",
                "currency": "INR"
            }
        return JSONResponse(
            status_code=200,
            content={
                "status": "fallback",
                "path": full_path,
                "init_error": str(e),
                "traceback": err_tb
            }
        )
