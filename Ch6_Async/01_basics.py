import asyncio
import time

# coroutine function
async def main():
    print('Hello')
    asyncio.sleep(10)
    print('World')

asyncio.run(main())