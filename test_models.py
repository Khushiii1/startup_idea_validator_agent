from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client()
for m in client.models.list():
    if "flash" in m.name:
        print(m.name)
