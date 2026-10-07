import os
import json
import logging
import requests
from backend.app.config import settings

logger = logging.getLogger('uvicorn')

class PaytmService:
    def __init__(self):
        self.mid = settings.PAYTM_MID
        self.merchant_key = settings.PAYTM_MERCHANT_KEY
        self.is_configured = bool(self.mid and self.merchant_key)

    def check_order_transaction_status(self, order_number: str) -> dict:
        """
        Queries Paytm Merchant Order Transaction Status API to confirm
        if payment has genuinely been credited to the merchant account.
        """
        if not self.is_configured:
            return {
                'configured': False,
                'is_paid': False,
                'status': 'PENDING',
                'message': 'Paytm Merchant MID not configured yet'
            }

        try:
            url = f"https://securegw.paytm.in/v3/order/status"
            paytm_params = {
                "body": {
                    "mid": self.mid,
                    "orderId": order_number
                },
                "head": {
                    "tokenType": "AES",
                    "signature": ""
                }
            }
            # Perform query
            response = requests.post(url, json=paytm_params, timeout=6)
            data = response.json()
            body = data.get("body", {})
            result_info = body.get("resultInfo", {})
            status = result_info.get("resultStatus", "")
            
            if status == "TXN_SUCCESS":
                return {
                    'configured': True,
                    'is_paid': True,
                    'status': 'TXN_SUCCESS',
                    'txn_id': body.get('txnId', ''),
                    'amount': float(body.get('txnAmount', 1.0)),
                    'message': 'Payment confirmed credited on Paytm merchant ledger.'
                }
            elif status == "PENDING":
                return {
                    'configured': True,
                    'is_paid': False,
                    'status': 'PENDING',
                    'message': 'Transaction is still processing on the banking network.'
                }
            else:
                return {
                    'configured': True,
                    'is_paid': False,
                    'status': 'FAILED',
                    'message': result_info.get('resultMsg', 'No transaction found.')
                }
        except Exception as e:
            logger.warning(f"Paytm status check error: {e}")
            return {
                'configured': True,
                'is_paid': False,
                'status': 'ERROR',
                'message': str(e)
            }

paytm_service = PaytmService()
