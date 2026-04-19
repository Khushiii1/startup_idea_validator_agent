import asyncio
import nest_asyncio
nest_asyncio.apply()
from app import run_validation_sync

print("Starting validation sync...")
result = run_validation_sync("New startup idea: AI tool for creating websites")
print("Result:", result)
