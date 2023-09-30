#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL"""


if __name__ == "__main__":
    import requests
    import sys

    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
