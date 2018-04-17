
import requests


def return_quotes():
    url = "https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['quotes']
    else:
        raise requests.ConnectionError("Expected status code 200. Client error")

def get_quotes():
    return return_quotes()

def get_quote(quote_num):
    return return_quotes()[quote_num]    

if __name__ == "__main__":
    print(get_quote(3))
