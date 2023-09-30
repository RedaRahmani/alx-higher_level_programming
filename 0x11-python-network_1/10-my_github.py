#!/usr/bin/python3
"""Uses Github credentials (username and password)
and Github API to display user id"""


if __name__ == "__main__":
    import requests
    import sys

    res = requests.get('https://api.github.com/user',
                       auth=(sys.argv[1], sys.argv[2]))
    if res.status_code >= 400:
        print('None')
    else:
        print(res.json().get('id'))
