import os

class Settings:
    APP_NAME: str = 'PULSE AUDIO Official Store'
    STORE_BRAND: str = 'PULSE AUDIO'
    API_PREFIX: str = '/api'
    HOST: str = os.getenv('HOST', '0.0.0.0')
    PORT: int = int(os.getenv('PORT', '8000'))
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'sqlite:///./pulse_audio.db')
    RAZORPAY_KEY_ID: str = os.getenv('RAZORPAY_KEY_ID', 'rzp_test_pulse_sandbox_key')
    RAZORPAY_KEY_SECRET: str = os.getenv('RAZORPAY_KEY_SECRET', 'pulse_secret_sandbox_signature_key')
    META_PIXEL_ID: str = os.getenv('META_PIXEL_ID', '102938475610293')
    META_CAPI_ACCESS_TOKEN: str = os.getenv('META_CAPI_ACCESS_TOKEN', '')
    META_TEST_EVENT_CODE: str = os.getenv('META_TEST_EVENT_CODE', '')

settings = Settings()
