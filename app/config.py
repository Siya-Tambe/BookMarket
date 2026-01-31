import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database Configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./bookmarket.db"  # Default to SQLite for local development
)

# Convert sqlite:// to sqlite:/// format if needed
if DATABASE_URL.startswith("sqlite://") and not DATABASE_URL.startswith("sqlite:///"):
    DATABASE_URL = DATABASE_URL.replace("sqlite://", "sqlite:///")

# For Supabase/PostgreSQL, ensure pool settings are configured
if "postgresql" in DATABASE_URL or "postgres" in DATABASE_URL:
    # Add connection pool settings for production
    DATABASE_URL = f"{DATABASE_URL}?sslmode=require"

# JWT Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-this-in-production")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

# App Configuration
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
