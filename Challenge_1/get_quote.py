#!/usr/bin/python3

import requests
import sys

def get_quote(quote_num):
    url = "https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes"
    response = requests.get(url).json()
    quote_list = response.get('quotes')
    return (quote_list[quote_num])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        quote_num = sys.argv[1]
    else:
        print ("Please provide a line number as input")
        sys.exit(1)

    if quote_num.isdigit():
        quote_num = int(quote_num)
        if quote_num < 0 or quote_num > 18:
            raise ValueError("Please enter a line number between 0 and 18.")
        else:
            print("Quote #{}:".format(quote_num))
            print(get_quote(quote_num))
    else:
        raise ValueError("Whoops! {} is not a number.".format(quote_num))
