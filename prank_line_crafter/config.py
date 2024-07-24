import os
from dotenv import load_dotenv

load_dotenv()

LLAMA_API_TOKEN = os.getenv("LLAMA_API_TOKEN")
URL = os.getenv("URL")

if not LLAMA_API_TOKEN or not URL:
    raise ValueError("Missing required environment variables: LLAMA_API_TOKEN or URL")
