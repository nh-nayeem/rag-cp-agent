import google.generativeai as genai
from typing import List
from .config import settings

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.text_model = genai.GenerativeModel("gemini-2.5-flash")
        self.embedding_model = "models/gemini-embedding-001"
    
    def generate_text(self, prompt: str) -> str:
        """Generate text using Gemini model."""
        try:
            response = self.text_model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Failed to generate text: {str(e)}")
    
    def embed_text(self, text: str) -> List[float]:
        """Generate embedding for text using Gemini."""
        try:
            embedding = genai.embed_content(
                model=self.embedding_model,
                content=text
            )
            return embedding['embedding']
        except Exception as e:
            raise Exception(f"Failed to generate embedding: {str(e)}")

gemini_client = GeminiClient()