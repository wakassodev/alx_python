#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""

import sys
import requests

if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()  # Raises HTTPError for bad responses
        print(response.text)
    except requests.exceptions.HTTPError as er:
        print('Error code:', er.response.status_code)