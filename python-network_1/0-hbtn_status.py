#!/usr/bin/python3
"""A script that
- uses requests and sys packages
"""
import requests
import sys

"""
- fetches https://alx-intranet.hbtn.io/status.
"""
if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    
    # Sending a GET request to the URL
    response = requests.get(url)
    
    # Retrieving the value of the X-Request-Id header
    x_request_id = response.headers.get('X-Request-Id')
    
    # Displaying the X-Request-Id value
    print(x_request_id)