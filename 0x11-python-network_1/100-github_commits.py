#!/usr/bin/python3
import requests
import sys
"""
a Python script that takes 2 arguments and
 list 10 commits (from the most recent to oldest) of the repository
"""


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Construct the GitHub API URL with line continuation
    url = (
        f"https://api.github.com/repos/{owner_name}/"
        f"{repository_name}/commits"
    )

    try:
        response = requests.get(url)
        commits = response.json()

        for commit in commits[:10]:  # Display the first 10 commits
            sha = commit.get("sha")
            author = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"JSON decoding error: {e}")
        sys.exit(1)
