#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL"""


if __name__ == "__main__":
    import sys
    import urllib.request

    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        page = response.read()
        header = response.info()
        print(dict(header).get("X-Request-Id"))
