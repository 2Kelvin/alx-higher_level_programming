#!/usr/bin/python3
"""Fetching GitHub commits using its api"""

if __name__ == '__main__':
    import sys
    import requests

    githubApiUrl = 'https://api.github.com/'
    fullUrl = f'{githubApiUrl}/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    httpResponse = requests.get(fullUrl)
    respToJson = httpResponse.json()
    for commit in respToJson[:10]:
        print(f'{commit["sha"]}:{commit["commit"]["author"]["name"]}')
