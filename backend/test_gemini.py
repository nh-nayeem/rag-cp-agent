from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load local .env
load_dotenv(dotenv_path=".env")

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing")

genai.configure(api_key=API_KEY)

# ----------------------------
# Test 1: LLM / text generate
# ----------------------------
def test_llm():
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content("Say a short random fact.")
    print("LLM Response:", response.text)


# ----------------------------
# Test 2: Embeddings
# ----------------------------
def test_embed():
    embedding = genai.embed_content(
        model="models/gemini-embedding-001",
        content="This is an embedding test."
    )
    print("Embedding vector length:", len(embedding['embedding']))

if __name__ == "__main__":
    # print("🔹 Testing Gemini LLM:")
    # test_llm()
    print("\n🔹 Testing Gemini Embedding:")
    test_embed()
