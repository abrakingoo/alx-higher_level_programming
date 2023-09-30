#!/usr/bin/python3
"""
 a Python script that takes in a URL, sends a request to the URL
 and displays the value of the X-Request-Id variable found in
 the header of the response
"""


if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from sys import argv

    url = argv[1]

    req = Request(url)
    with urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
