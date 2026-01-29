# BookMarket - Second Hand Book Marketplace

A full-stack web application for buying and selling second-hand books at discounted prices.

## Live Demo

- **Deployed URL** (Render):  
  https://bookmarket-mayurroro.onrender.com/

All backend APIs and frontend pages (home, login, browse books, profile, payment) are served from this URL.

## Features

- **User Authentication**: Secure login and registration system using JWT
- **Book Listings**: Browse available second-hand books for sale
- **Book Management**: List your own books with details (title, author, price, condition, category, image, etc.)
- **User Profile**: View all your listed books and see whether they are sold or still available
- **Buy Flow with Dummy Payment**:
  - `Buy Now` button on the Browse Books page
  - Redirects to a **Payment** page with a dummy payment form (Card / UPI / Netbanking)
  - After a successful dummy payment, the book is marked as **sold**
- **Sold Book Handling**: Sold books are automatically **hidden** from the Browse Books page but remain visible in the seller’s profile
- **Discounted Pricing**: Shows both original price and discounted selling price, with percentage discount badge
- **Indian Currency (INR)**: All prices are displayed in **₹ (INR)**
- **Modern UI**: Clean, responsive layout built with HTML, CSS and JavaScript

## Tech Stack

- **Backend**: Python with FastAPI
- **Database**: SQLite (SQL database)
- **Authentication**: JWT tokens (`python-jose`)
- **ORM**: SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript (served via FastAPI templates)
- **Deployment**: Render (single service running FastAPI app)

## Installation (Local Development)

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

## Running the Application Locally

You can run the app either with `uvicorn` directly or via the helper script.

### Option 1: Using `uvicorn`

```bash
uvicorn app.main:app --reload
```

### Option 2: Using `run.py`

```bash
python run.py
```

Then open your browser and navigate to:

```text
http://localhost:8000
```

The application will automatically create the SQLite database (`bookmarket.db`) on first run.

## Project Structure

```text
BookMarket/
├── Demonstration_Video/
│   └── EPD project demonstration.mp4
├── app/
│   ├── __init__.py
│   ├── app.py           # ASGI entrypoint (from .main import app)
│   ├── main.py          # FastAPI application, routes & HTML pages
│   ├── database.py      # Database configuration (SQLite + SQLAlchemy)
│   ├── models.py        # SQLAlchemy models (User, Book)
│   ├── schemas.py       # Pydantic schemas (request/response models)
│   └── auth.py          # Authentication utilities (JWT + bcrypt)
├── templates/
│   ├── index.html       # Home page
│   ├── login.html       # Login/Register page
│   ├── books.html       # Book listings page (Browse Books)
│   ├── profile.html     # User profile page
│   └── payment.html     # Dummy payment page (Buy flow)
├── static/
│   ├── css/
│   │   └── style.css    # Stylesheet
│   └── js/
│       └── app.js       # Frontend JavaScript (auth checks, book loading, etc.)
├── create_test_user.py  # Helper script to create a default test user
├── run.py               # Helper script to run uvicorn with reload
├── render.yaml          # Render deployment configuration
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## API Endpoints

### Authentication

- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and get access token
- `GET /api/auth/me` - Get current user info (requires authentication)

### Books

- `GET /api/books` - Get all available (not sold) books
- `GET /api/books/{book_id}` - Get a specific book by ID
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
- `price`: Selling price (in INR)
- `original_price`: Original price (for discount calculation, in INR)
- `condition`: Book condition (New, Like New, Good, Fair, Poor)
- `category`: Book category
- `image_url`: Book cover image URL
- `is_sold`: Whether the book is sold
- `seller_id`: Foreign key to `users.id`
- `created_at`: Listing creation timestamp
- `sold_at`: Sale timestamp (if sold)

## Usage

1. **Register/Login**: Create an account or login with existing credentials.
2. **Browse Books**: View all available books on the Browse Books page.
3. **List a Book**: Click **“+ Add Book”** to list your own book for sale.
4. **Buy a Book**: Click **“Buy Now”** on a book to go to the Payment page and complete a dummy payment.
5. **Manage Your Books**: Go to your profile to see all your listed books (sold and available).
6. **Mark as Sold / Delete**: From your profile, mark books as sold (if not using the payment flow) or delete listings.

## Security Notes

- Change the `SECRET_KEY` in `app/auth.py` for production use.
- Consider using environment variables (e.g. `.env`) for sensitive configuration (secrets, DB URLs, etc.).
- For production, prefer a more robust database (e.g. PostgreSQL) instead of SQLite.
- Implement stricter CORS policies for production instead of `allow_origins=["*"]`.

## License

This project is open source and available for educational purposes.
