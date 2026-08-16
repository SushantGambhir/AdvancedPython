import time
import asyncio

# Normal sync API calls

# def api_call():
#     time.sleep(3)
#     return 'Orders data'

# def execute():
#     print('Executing API call')
#     result = api_call()
#     print('Data Fetched: ', result)

# execute()

async def api_call():
    await asyncio.sleep(3)
    return 'Orders data'

async def execute():
    print('Executing API call')
    result = await api_call()
    print('Data Fetched: ', result)

asyncio.run(execute())