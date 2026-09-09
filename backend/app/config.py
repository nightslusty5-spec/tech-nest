import os

class Settings:
    APP_NAME: str = 'PULSE AUDIO Official Store'
    STORE_BRAND: str = 'PULSE AUDIO'
    API_PREFIX: str = '/api'
    HOST: str = os.getenv('HOST', '0.0.0.0')
    PORT: int = int(os.getenv('PORT', '8000'))
    
    # On Vercel serverless functions, root filesystem is read-only.
    # We must write SQLite database to /tmp/ or use external DATABASE_URL.
    is_vercel: bool = bool(os.getenv('VERCEL'))
    default_db_path: str = '/tmp/pulse_audio.db' if is_vercel else './pulse_audio.db'
    DATABASE_URL: str = os.getenv('DATABASE_URL', f'sqlite:///{default_db_path}')
    
    RAZORPAY_KEY_ID: str = os.getenv('RAZORPAY_KEY_ID', 'rzp_test_pulse_sandbox_key')
    RAZORPAY_KEY_SECRET: str = os.getenv('RAZORPAY_KEY_SECRET', 'pulse_secret_sandbox_signature_key')
    META_PIXEL_ID: str = os.getenv('META_PIXEL_ID', '102938475610293')
    META_CAPI_ACCESS_TOKEN: str = os.getenv('META_CAPI_ACCESS_TOKEN', '')
    META_TEST_EVENT_CODE: str = os.getenv('META_TEST_EVENT_CODE', '')

settings = Settings()
