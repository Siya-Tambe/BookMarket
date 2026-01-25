"""
Script to add sample books to the BookMarket database
"""
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from app.database import SessionLocal as DefaultSessionLocal, engine as default_engine
from app import models
import sys
import os
import bcrypt

# Create tables if they don't exist
models.Base.metadata.create_all(bind=default_engine)

def create_sample_user(db: Session):
    """Create a sample user if one doesn't exist"""
    user = db.query(models.User).filter(models.User.username == "admin").first()
    if not user:
        # Use direct bcrypt to avoid passlib issues
        password = "admin123"
        # Hash password using bcrypt directly
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
        
        user = models.User(
            username="admin",
            email="admin@bookmarket.com",
            hashed_password=hashed,
            full_name="Admin User"
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        print(f"Created user: {user.username} (ID: {user.id})")
    else:
        print(f"Using existing user: {user.username} (ID: {user.id})")
    return user

def add_books(db: Session, seller_id: int):
    """Add sample books to the database"""
    
    # Prices converted from USD to INR (approximate rate: 1 USD = 83 INR)
    sample_books = [
        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "isbn": "978-0-7432-7356-5",
            "description": "A classic American novel about the Jazz Age and the American Dream.",
            "price": 1245.00,
            "original_price": 750.00,
            "condition": "Like New",
            "category": "Fiction",
            "image_url": "https://images-na.ssl-images-amazon.com/images/I/81QuEGw8VPL.jpg"
        },
        {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "isbn": "978-0-06-112008-4",
            "description": "A gripping tale of racial injustice and childhood innocence in the American South.",
            "price": 625.00,
            "original_price": 1078.00,
            "condition": "Good",
            "category": "Fiction",
            "image_url": "https://images-na.ssl-images-amazon.com/images/I/81gepf1eMqL.jpg"
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "isbn": "978-0-452-28423-4",
            "description": "A dystopian novel about totalitarianism and surveillance.",
            "price": 1327.00,
            "original_price": 830.00,
            "condition": "Good",
            "category": "Science Fiction",
            "image_url": "https://images-na.ssl-images-amazon.com/images/I/81StSOpmkjL.jpg"
        },
        {
            "title": "Pride and Prejudice",
            "author": "Jane Austen",
            "isbn": "978-0-14-143951-8",
            "description": "A romantic novel of manners about Elizabeth Bennet and Mr. Darcy.",
            "price": 899.00,
            "original_price": 599.00,
            "condition": "Like New",
            "category": "Romance",
            "image_url": "https://images-na.ssl-images-amazon.com/images/I/71Q1tPupKjL.jpg"
        },
        {
            "title": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "isbn": "978-0-316-76948-0",
            "description": "A controversial novel about teenage rebellion and alienation.",
            "price": 1161.00,
            "original_price": 705.00,
            "condition": "Fair",
            "category": "Fiction",
            "image_url": "https://images-na.ssl-images-amazon.com/images/I/81OthjkJBuL.jpg"
        },
        {
            "title": "Harry Potter and the Philosopher's Stone",
            "author": "J.K. Rowling",
            "isbn": "978-0-7475-3269-6",
            "description": "The first book in the magical Harry Potter series.",
            "price": 1493.00,
            "original_price": 912.00,
            "condition": "New",
            "category": "Fantasy",
            "image_url": "https://images-na.ssl-images-amazon.com/images/I/81YOuOGFCJL.jpg"
        },
        {
            "title": "The Lord of the Rings",
            "author": "J.R.R. Tolkien",
            "isbn": "978-0-544-00020-2",
            "description": "An epic fantasy trilogy about the quest to destroy the One Ring.",
            "price": 1659.00,
            "original_price": 1078.00,
            "condition": "Good",
            "category": "Fantasy",
            "image_url": "https://images-na.ssl-images-amazon.com/images/I/71jLBXtWJWL.jpg"
        },
        {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "isbn": "978-0-06-112241-5",
            "description": "A philosophical novel about following your dreams.",
            "price": 1245.00,
            "original_price": 789.00,
            "condition": "Like New",
            "category": "Philosophy",
            "image_url": "https://images-na.ssl-images-amazon.com/images/I/71aFt4+OTOL.jpg"
        },
        {
            "title": "Sapiens: A Brief History of Humankind",
            "author": "Yuval Noah Harari",
            "isbn": "978-0-06-231609-7",
            "description": "A fascinating exploration of how Homo sapiens conquered the world.",
            "price": 1576.00,
            "original_price": 995.00,
            "condition": "Good",
            "category": "History",
            "image_url": "https://images-na.ssl-images-amazon.com/images/I/81yu0X2htjL.jpg"
        },
        {
            "title": "The Hunger Games",
            "author": "Suzanne Collins",
            "isbn": "978-0-439-02348-1",
            "description": "A dystopian novel about a televised fight to the death.",
            "price": 750.00,
            "original_price": 1245.00,
            "condition": "Like New",
            "category": "Young Adult",
            "image_url": "https://images-na.ssl-images-amazon.com/images/I/61JfGcL2ljL.jpg"
        }
    ]
    
    added_count = 0
    for book_data in sample_books:
        # Check if book already exists
        existing = db.query(models.Book).filter(
            models.Book.title == book_data["title"],
            models.Book.author == book_data["author"],
            models.Book.seller_id == seller_id
        ).first()
        
        if not existing:
            book = models.Book(**book_data, seller_id=seller_id)
            db.add(book)
            added_count += 1
            print(f"Added: {book_data['title']} by {book_data['author']}")
        else:
            print(f"Skipped (already exists): {book_data['title']} by {book_data['author']}")
    
    db.commit()
    print(f"\nSuccessfully added {added_count} new books to the database!")
    return added_count

def main():
    # Check if custom database path is provided
    if len(sys.argv) > 1:
        db_path = sys.argv[1]
        # Use absolute path for SQLite
        if os.path.isabs(db_path):
            db_url = f"sqlite:///{db_path}"
        else:
            db_url = f"sqlite:///{os.path.abspath(db_path)}"
        
        print(f"Using database: {db_path}")
        engine = create_engine(db_url, connect_args={"check_same_thread": False})
        # Drop existing tables and recreate with correct schema
        print("Recreating database tables with correct schema...")
        models.Base.metadata.drop_all(bind=engine)
        models.Base.metadata.create_all(bind=engine)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
    else:
        print("Using default database location...")
        models.Base.metadata.create_all(bind=default_engine)
        db = DefaultSessionLocal()
    
    try:
        # Create a sample user
        user = create_sample_user(db)
        
        # Add books
        add_books(db, user.id)
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()
