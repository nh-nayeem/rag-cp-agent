import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url = os.getenv("QDRANT_URL")
api_key = os.getenv("QDRANT_API_KEY")

print(f"QDRANT_URL: {url}")
print(f"QDRANT_API_KEY: {api_key}")

if not url or not api_key:
    print("ERROR: QDRANT_URL or QDRANT_API_KEY environment variables are not set!")
    print("Please create a .env file with these variables or set them in your environment.")
    exit(1)

try:
    # Test API key by getting collections
    headers = {"api-key": api_key}
    res = requests.get(f"{url}/collections", headers=headers, timeout=10)
    
    print(f"Status Code: {res.status_code}")
    
    if res.status_code == 200:
        print("SUCCESS: API key is valid and connection successful!")
        print("Collections:", res.json())
    else:
        print(f"ERROR: API request failed with status {res.status_code}")
        print("Response:", res.text)
        
except requests.exceptions.RequestException as e:
    print(f"ERROR: Connection failed - {e}")
    print("Please check your QDRANT_URL and internet connection.")
