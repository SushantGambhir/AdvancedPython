def my_decorator(func):
    def mainfunc(*args): # Will have all the input arguments of the function being passed
        print('Before')
        response = func(*args)
        print('After')
        return response

    return mainfunc

@my_decorator
def fetch_data(url,path):
    print('Fetching data from '+ url + ' to the path ' + path)

fetch_data("https://example.com/data","/tmp/data.csv")
