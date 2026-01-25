"""
Script to create a default test user for BookMarket
"""
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models
import bcrypt

def create_test_user():
    """Create a default test user"""
    db: Session = SessionLocal()
    
    try:
        # Check if test user already exists
        user = db.query(models.User).filter(models.User.username == "testuser").first()
        
        if user:
            print(f"Test user already exists!")
            print(f"Username: {user.username}")
            print(f"Email: {user.email}")
            print(f"Full Name: {user.full_name}")
            return user
        
        # Create test user
        password = "test123"
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt).decode('utf-8')
        
        user = models.User(
            username="testuser",
            email="test@bookmarket.com",
            hashed_password=hashed,
            full_name="Test User"
        )
        
        db.add(user)
        db.commit()
        db.refresh(user)
        
        print("=" * 50)
        print("TEST USER CREATED SUCCESSFULLY!")
        print("=" * 50)
        print(f"Username: {user.username}")
        print(f"Password: {password}")
        print(f"Email: {user.email}")
        print(f"Full Name: {user.full_name}")
        print("=" * 50)
        print("\nYou can now use these credentials to login at:")
        print("http://localhost:8000/login")
        print("=" * 50)
        
        return user
        
    except Exception as e:
        print(f"Error creating test user: {e}")
        db.rollback()
        return None
    finally:
        db.close()

if __name__ == "__main__":
    create_test_user()
