import os
import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()
        
        upi_id = os.environ.get('PAYTM_UPI_ID', 'paytm.pulse@paytm')
        merchant_name = os.environ.get('PAYTM_MERCHANT_NAME', 'PULSE AUDIO Official')
        
        response = {
            'upi_id': upi_id,
            'merchant_name': merchant_name,
            'store_name': 'PULSE AUDIO',
            'currency': 'INR'
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()
        return
