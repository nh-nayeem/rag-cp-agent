import os
from dotenv import load_dotenv
from typing import Optional

# Load .env only if local (for development)
if os.path.exists(".env"):
    load_dotenv()

class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    QDRANT_URL: str = os.getenv("QDRANT_URL", "")
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY", "")
    QDRANT_COLLECTION_NAME: str = os.getenv("QDRANT_COLLECTION_NAME", "cp_documents")
    
    def __init__(self):
        if not self.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is required")
        if not self.QDRANT_URL:
            raise ValueError("QDRANT_URL is required")

settings = Settings()