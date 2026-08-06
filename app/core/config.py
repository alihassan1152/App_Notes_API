# ============================================
# Config — saare environment variables ek jagah
# ============================================
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "smart_notes_db")

# AI Service (OmniRoute)
OMNIROUTE_KEY = os.getenv("OMNIROUTE_KEY")
OMNIROUTE_URL = os.getenv("OMNIROUTE_URL")
