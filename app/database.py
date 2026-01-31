from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool, QueuePool
from app.config import DATABASE_URL, ENVIRONMENT
from urllib.parse import urlparse, urlunparse

# Determine if using PostgreSQL (Supabase) or SQLite
is_postgresql = "postgresql" in DATABASE_URL or "postgres" in DATABASE_URL

# Create engine with appropriate pool configuration
if is_postgresql:
    # PostgreSQL/Supabase configuration
    engine = create_engine(
        DATABASE_URL,
        poolclass=QueuePool,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,  # Verify connections are alive
        pool_recycle=3600,   # Recycle connections every hour
        echo=False
    )
else:
    # SQLite configuration (local development)
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=NullPool  # SQLite doesn't benefit from connection pooling
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    Dependency for getting database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """
    Initialize database tables. If connection fails, log a warning but don't crash the app.
    """
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.warning(f"Database initialization skipped (connection failed): {e}")


def _mask_db_url(url: str) -> str:
    try:
        p = urlparse(url)
        if p.username:
            netloc = f"{p.username}:*****@{p.hostname}"
            if p.port:
                netloc += f":{p.port}"
            return urlunparse((p.scheme, netloc, p.path, p.params, p.query, p.fragment))
    except Exception:
        pass
    return url


def get_db_info() -> dict:
    """Return a small dict with DB type and masked URL for diagnostics."""
    return {
        "is_postgresql": is_postgresql,
        "database_url_masked": _mask_db_url(DATABASE_URL),
    }
