import os
from dotenv import load_dotenv

load_dotenv()

# Configuration Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL", "votre_url_supabase")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "votre_anon_key")

# Configuration Locale
LOCAL_DB = "base.db"
SYNC_INTERVAL = 600  # 10 minutes en secondes
