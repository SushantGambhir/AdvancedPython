class api_fetch:
    def fetch(self):
        print("Fetching data from API...")

class database_fetch:
    def fetch(self):
        print("Fetching data from Database...")

class blob_fetch:
    def fetch(self):
        print("Fetching data from blob...")

obj = database_fetch()
obj.fetch()

# Here we have a function with same name (fetch()) with different functionalities and class names