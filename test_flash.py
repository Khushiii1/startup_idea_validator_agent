from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

models = ["gemini-flash-latest"]

for m in models:
    try:
        response = client.models.generate_content(
            model=m,
            contents="Say hello"
        )
        print(f"Success! {m} works. Output: {response.text}")
    except Exception as e:
        print(f"Failed {m}: {str(e)}")
