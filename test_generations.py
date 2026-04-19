from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client()

models = [
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash-lite",
    "gemini-flash-lite-latest"
]

for m in models:
    print(f"Testing {m}...")
    try:
        response = client.models.generate_content(
            model=m,
            contents="Say hello"
        )
        print(f"Success! {m} works.")
    except Exception as e:
        print(f"Failed {m}: {str(e)}")
