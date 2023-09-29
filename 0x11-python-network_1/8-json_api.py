#!/usr/bin/python3
# Search API (JSON)

if __name__ == '__main__':
    import requests
    import sys

    if sys.argv[1] is None:
        q = ''
    else:
        q = sys.argv[1]
    qData = {'q': q}
    serverUrl = 'http://0.0.0.0:5000/search_user'
    httpResponse = requests.post(serverUrl, qData)
    try:
        outpt = httpResponse.json()
        if outpt:
            print(f'[{outpt.get("id")}] {outpt.get("name")}')
        else:
            print('No result')
    except:
        print('Not a valid JSON')
