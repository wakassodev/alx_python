#!/usr/bin/python3
"""A script that
- uses urlib package
"""
from urllib import requests

if __name__ == '__main__':
    
    """
    - fetches https://alx-intranet.hbtn.io/status.
    """
    with requests.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))