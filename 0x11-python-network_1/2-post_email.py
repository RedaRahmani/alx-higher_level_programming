#!/usr/bin/python3
""" script that takes in a URL and email, sends a request to the URL."""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8", "replace"))
