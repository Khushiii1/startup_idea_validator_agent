import asyncio
from main import run_validation

async def main():
    print("Run 1...")
    await run_validation("Idea 1")
    print("Run 2...")
    await run_validation("Idea 2")

asyncio.run(main())
