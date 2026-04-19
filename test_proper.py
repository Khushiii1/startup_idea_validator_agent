import asyncio
import nest_asyncio
import uuid

nest_asyncio.apply()
from main import run_validation

idea = "A platform that uses AI to generate personalized bedtime stories for kids based on their daily activities"
print(f"Testing idea: {idea}")
try:
    asyncio.run(run_validation(idea))
except Exception as e:
    print(f"Exception caught: {e}")
