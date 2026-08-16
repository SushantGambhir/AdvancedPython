import time
import asyncio

async def api_call(url: str, delay: int):
    print('Fetching data from: ', url)
    await asyncio.sleep(delay)
    print('Data fetched from: ', url)
    return f'{url} data'

async def main():
    # Creating Tasks with gather
    tasks = await asyncio.gather(
        api_call("https://api1.com",2),
        api_call("https://api2.com",3),
        api_call("https://api3.com",1)
    )
     # Another way to create tasks with list comprehension
     # tasks = [api_call(url) for url in ['https://api1.com','https://api2.com','https://api3.com']]
     # results = await asyncio.gather(*tasks)
    print('All API calls completed')

asyncio.run(main())