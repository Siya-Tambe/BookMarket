# BookMarket - Second Hand Book Marketplace

A full-stack web application for buying and selling second-hand books at discounted prices.

## Live Demo

- **Deployed URL** (Render):  
  https://bookmarket-mayurroro.onrender.com/

All backend APIs and frontend pages (home, login, browse books, profile, payment) are served from this URL.

## Features

- **User Authentication**: Secure login and registration system
- **Book Listings**: Browse available books for sale
- **Book Management**: List your own books with details (title, author, price, condition, etc.)
- **User Profile**: View your listed books and their status (sold/available)
- **Discounted Pricing**: Display original and discounted prices
- **Modern UI**: Beautiful, responsive design

## Tech Stack

- **Backend**: Python with FastAPI
- **Database**: SQLite (SQL database)
- **Authentication**: JWT tokens
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL (via Supabase) - SQLite for local development
- **Authentication**: JWT tokens (`python-jose`)
- **ORM**: SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript (served via FastAPI templates)
- **Deployment**: Render (single service running FastAPI app)

## Installation

1. **Clone or navigate to the project directory**

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv
```

3. **Activate the virtual environment**:
   - On Windows:
   ```bash
   venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Running the Application

1. **Start the FastAPI server**:
```bash
uvicorn app.main:app --reload
```

2. **Open your browser** and navigate to:
```
http://localhost:8000
```

The application will automatically create the SQLite database (`bookmarket.db`) on first run.

## Supabase Integration (for Production/Hosting)

**Important**: SQLite data is lost when the server restarts on hosting platforms. To persist data in production:

### Quick Setup for Render Deployment

1. **Create a free Supabase account** at https://supabase.com
2. **Create a new Supabase project** and get your PostgreSQL connection string
3. **In your Render dashboard**, add environment variables:
   - `DATABASE_URL`: Your Supabase PostgreSQL connection string
   - `SECRET_KEY`: A strong random secret key

4. **Deploy** - the app will automatically create tables in Supabase

### Local Testing with Supabase

1. **Create `.env` file** in project root (copy from `.env.example`):
   ```
   DATABASE_URL=postgresql://postgres:password@host.supabase.co:5432/postgres
   SECRET_KEY=your-secret-key
   ```

2. **Run the app** - it will use Supabase:
   ```bash
   python run.py
   ```

📖 **[Full Supabase Integration Guide](SUPABASE_SETUP.md)** - Step-by-step instructions for setup

### Why Supabase for Production?

- ✅ Data persists across server restarts and deployments
- ✅ Scalable PostgreSQL database
- ✅ Free tier suitable for small projects
- ✅ Automatic backups
- ✅ Easy to setup and manage

## Project Structure

```
BookMarket/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application and routes
│   ├── database.py      # Database configuration
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   └── auth.py          # Authentication utilities
│   ├── app.py           # ASGI entrypoint (from .main import app)
│   ├── main.py          # FastAPI application, routes & HTML pages
│   ├── database.py      # Database configuration (PostgreSQL/SQLite)
│   ├── models.py        # SQLAlchemy models (User, Book)
│   ├── schemas.py       # Pydantic schemas (request/response models)
│   ├── auth.py          # Authentication utilities (JWT + bcrypt)
│   └── config.py        # Configuration and environment variables
├── templates/
│   ├── index.html       # Home page
│   ├── login.html       # Login/Register page
│   ├── books.html       # Book listings page
│   └── profile.html     # User profile page
├── static/
│   ├── css/
│   │   └── style.css    # Stylesheet
│   └── js/
│       └── app.js       # Frontend JavaScript
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and get access token
- `GET /api/auth/me` - Get current user info (requires authentication)

### Books
- `GET /api/books` - Get all available books
- `GET /api/books/{book_id}` - Get a specific book
- `POST /api/books` - Create a new book listing (requires authentication)
- `PUT /api/books/{book_id}` - Update a book (requires authentication, owner only)
- `DELETE /api/books/{book_id}` - Delete a book (requires authentication, owner only)

### User Profile
- `GET /api/users/me/books` - Get current user's books (requires authentication)

## Database Schema

### Users Table
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email
- `hashed_password`: Encrypted password
- `full_name`: User's full name
- `created_at`: Account creation timestamp

### Books Table
- `id`: Primary key
- `title`: Book title
- `author`: Book author
- `isbn`: International Standard Book Number (optional)
- `description`: Book description
- `price`: Selling price
- `original_price`: Original price (for discount calculation)
- `condition`: Book condition (New, Like New, Good, Fair, Poor)
- `category`: Book category
- `image_url`: Book cover image URL
- `is_sold`: Whether the book is sold
- `seller_id`: Foreign key to users table
- `created_at`: Listing creation timestamp
- `sold_at`: Sale timestamp (if sold)

## Usage

1. **Register/Login**: Create an account or login with existing credentials
2. **Browse Books**: View all available books on the books page
3. **List a Book**: Click "Add Book" to list your own book for sale
4. **Manage Your Books**: Go to your profile to see all your listed books
5. **Mark as Sold**: Update the status of your books when they're sold

## Security Notes

- Change the `SECRET_KEY` in `app/auth.py` for production use
- Consider using environment variables for sensitive configuration
- For production, use a more robust database (PostgreSQL) instead of SQLite
- Implement proper CORS policies for production
- **Change the `SECRET_KEY`** in `app/config.py` or use environment variables for production
- **Use environment variables** for sensitive configuration (`.env` file, never committed to git)
- **For production**: Use PostgreSQL (Supabase) instead of SQLite
- **Implement stricter CORS policies** for production instead of `allow_origins=["*"]`
- **Use `.env.example`** as a template - copy to `.env` and fill in actual values
- **Keep `.env` file in `.gitignore`** - never commit credentials

## License

This project is open source and available for educational purposes.
