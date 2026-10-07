import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.app.config import settings

logger = logging.getLogger("uvicorn")

db_url = settings.DATABASE_URL
if db_url.startswith('postgres://'):
    db_url = db_url.replace('postgres://', 'postgresql://', 1)

try:
    connect_args = {'check_same_thread': False} if 'sqlite' in db_url else {}
    engine = create_engine(db_url, connect_args=connect_args, echo=False)
    # Test connection
    with engine.connect() as conn:
        pass
except Exception as e:
    logger.warning(f"Database connection to {db_url} failed: {e}. Falling back to SQLite in /tmp.")
    fallback_path = '/tmp/pulse_audio_fallback.db' if os.path.exists('/tmp') else './pulse_audio_fallback.db'
    db_url = f'sqlite:///{fallback_path}'
    connect_args = {'check_same_thread': False}
    engine = create_engine(db_url, connect_args=connect_args, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
