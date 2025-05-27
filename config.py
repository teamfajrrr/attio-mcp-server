import os
from dotenv import load_dotenv

# Load .env from the project root (same directory as this config.py)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

BASE_URL = os.getenv("BASE_URL", "https://api.attio.com")
API_KEY = os.getenv("API_KEY")
PORT = os.environ.get("PORT", "8080")  # This returns a string
TRANSPORT = os.getenv("TRANSPORT", "sse")
