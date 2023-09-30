#!/usr/bin/python3
"""
 a Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    from urllib.request import urlopen
    with urlopen("https://alx-intranet.hbtn.io/status") as res:
        body = res.read()

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
