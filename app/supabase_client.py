from supabase import create_client, Client
from app.config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = None

if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
else:
    import logging
    logging.getLogger("uvicorn.error").warning("Supabase credentials missing. Cloud storage will be disabled.")
