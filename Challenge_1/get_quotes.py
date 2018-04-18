#!/usr/bin/python3

import requests

def get_quotes():
    url = "https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes"
    res_dct = {}
    response = requests.get(url).json()
    for idx, quote in enumerate(response.get('quotes')):
        res_dct[idx] = quote
    print("Here are all quotes available:")
    return res_dct

if __name__ == "__main__":
    print(get_quotes())
