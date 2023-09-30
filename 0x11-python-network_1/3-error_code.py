#!/usr/bin/python3
""" sends a request to the URL supplied"""


if __name__ == "__main__":
    import sys
    import urllib.request
    from urllib.error import HTTPError

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8", "replace"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
