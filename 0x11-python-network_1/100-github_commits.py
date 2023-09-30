#!/usr/bin/python3
import requests
import sys
"""
a Python script that takes 2 arguments and
 list 10 commits (from the most recent to oldest) of the repository
"""


if __name__ == "__main__":

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = (
        f"https://api.github.com/repos/{owner_name}/"
        f"{repository_name}/commits"
    )
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author}")
