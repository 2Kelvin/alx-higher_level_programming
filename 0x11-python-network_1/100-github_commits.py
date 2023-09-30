#!/usr/bin/python3
"""Fetching GitHub commits using its api"""

if __name__ == '__main__':
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]
    githubApiUrl = 'https://api.github.com'
    fullUrl = f'{githubApiUrl}/repos/{owner}/{repo}/commits'
    httpResponse = requests.get(fullUrl)
    # print(httpResponse.text, '\n')
    commits = httpResponse.json()
    for i in range(0, 10):
        print(f'{commits[i].get("sha")}: \
              {commits[i].get("commit").get("author").get("name")}')
