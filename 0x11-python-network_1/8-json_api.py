#!/usr/bin/python3
"""Takes in a letter and sends a POST request to URL"""


if __name__ == "__main__":
    import requests
    import sys

    query = ""
    if len(sys.argv) > 1:
        query = sys.argv[1]
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': query})
    try:
        result = res.json()
        if result == {}:
            print('No result')
        else:
            print("[{}] {}".format(result.get('id'), result.get('name')))
    except ValueError:
        print('Not a valid JSON')
