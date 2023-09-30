#!/usr/bin/python3
"""Takes in a URL and an email address, sends a POST request to the URL"""


if __name__ == "__main__":
    import requests
    import sys

    res = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(res.text)
