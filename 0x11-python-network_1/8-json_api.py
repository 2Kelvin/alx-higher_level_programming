#!/usr/bin/python3
"""Search API (JSON)"""

if __name__ == '__main__':
    import requests
    import sys

    if sys.argv[1] is None:
        q = ''
    else:
        q = sys.argv[1]
    qData = {'q': q}
    serverUrl = 'http://0.0.0.0:5000/search_user'
    httpResponse = requests.post(serverUrl, data=qData)
    try:
        outpt = httpResponse.json()
        if outpt == {}:
            print('No result')
        else:
            print("[{}] {}".format(outpt.get("id"), outpt.get("name")))
    except ValueError:
        print('Not a valid JSON')
