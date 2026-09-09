import hashlib
import time
import requests
from backend.app.config import settings

class MetaCAPIService:
    def __init__(self):
        self.pixel_id = settings.META_PIXEL_ID
        self.access_token = settings.META_CAPI_ACCESS_TOKEN
        self.test_event_code = settings.META_TEST_EVENT_CODE

    @staticmethod
    def _hash_field(value: str) -> str:
        if not value:
            return ''
        clean_val = value.strip().lower()
        return hashlib.sha256(clean_val.encode('utf-8')).hexdigest()

    def send_event(self, event_name: str, event_id: str, user_data: dict, custom_data: dict, source_url: str = ''):
        if not self.pixel_id or not self.access_token:
            val = custom_data.get('value', 0)
            print(f'[Meta CAPI Simulated] {event_name} - event_id: {event_id}, value: {val} INR')
            return {'status': 'simulated', 'event_name': event_name, 'event_id': event_id}
        payload_user_data = {}
        if user_data.get('email'):
            payload_user_data['em'] = [self._hash_field(user_data['email'])]
        if user_data.get('phone'):
            p = user_data['phone'].replace('+', '').replace('-', '').strip()
            if len(p) == 10:
                p = f'91{p}'
            payload_user_data['ph'] = [self._hash_field(p)]
        if user_data.get('first_name'):
            payload_user_data['fn'] = [self._hash_field(user_data['first_name'])]
        if user_data.get('city'):
            payload_user_data['ct'] = [self._hash_field(user_data['city'])]
        if user_data.get('state'):
            payload_user_data['st'] = [self._hash_field(user_data['state'])]
        if user_data.get('pincode'):
            payload_user_data['zp'] = [self._hash_field(user_data['pincode'])]
        payload_user_data['country'] = [self._hash_field('in')]
        event_payload = {
            'event_name': event_name,
            'event_time': int(time.time()),
            'event_id': event_id,
            'event_source_url': source_url or 'https://pulseaudio.in/product/pulse-sonic-pro',
            'action_source': 'website',
            'user_data': payload_user_data,
            'custom_data': custom_data
        }
        url = f'https://graph.facebook.com/v19.0/{self.pixel_id}/events'
        body = {'data': [event_payload], 'access_token': self.access_token}
        if self.test_event_code:
            body['test_event_code'] = self.test_event_code
        try:
            res = requests.post(url, json=body, timeout=8)
            return res.json()
        except Exception as e:
            print(f'[Meta CAPI Error]: {e}')
            return {'status': 'error', 'error': str(e)}

meta_capi = MetaCAPIService()
