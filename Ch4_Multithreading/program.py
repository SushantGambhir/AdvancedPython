import time
from concurrent.futures import ThreadPoolExecutor

def fetch_data(url: str):
    print("Fetching data from:", url)
    time.sleep(5)
    print("Data fetched from:", url)
    return "Data from " + url

urls_list = ["https://example.com/api/data1", 
             "https://example.com/api/data2", 
             "https://example.com/api/data3", 
             "https://example.com/api/data4", 
             "https://example.com/api/data5"]

# Traditional brute force way to have this function called for each url defined in the above list, we would do it as follows:
# for i in urls_list:
#     fetch_data(i)
# However what if there are 1000s of URLs and data is big, it takes time to fetch data. It will too slow
# Hence we shall be using the multithreading

results = []
with ThreadPoolExecutor(max_workers=len(urls_list)) as executor:
    futures = executor.map(fetch_data,urls_list)
# Alternatively the above statement can also be used as:
#    futures = [executor.submit(fetch_data,url) for url in urls_list]
    results.extend(futures)

print(results)

# In the above example the function is only expecting one argument (url: string). 
# If multiple arguments are needed then use dictionary and pass key