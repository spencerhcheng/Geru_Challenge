import requests


def return_quotes():
    """
    Returns all quotes provided by API upon success
    """
    url = "https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['quotes']
    else:
        raise requests.ConnectionError("Expected status code 200. Client error")

def get_quotes():
    """
    Returns all quotes
    """
    return return_quotes()

def get_quote(quote_number):
    """
    Returns quote number followed by quote
    """
    if not quote_number.isdigit() or int(quote_number) < 0 or int(quote_number) > 18:
        error_msg = "Please enter a number between 0 and 18!"
        return error_msg
    else:
        return quote_number + " : " + return_quotes()[int(quote_number)]
