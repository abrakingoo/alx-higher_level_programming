#!/usr/bin/env bash
# a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
url="$1"
curl -Is "$url" | grep Content-Length | awk '{print $2}'
