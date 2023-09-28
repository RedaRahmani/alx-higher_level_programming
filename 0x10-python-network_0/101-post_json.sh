#!/bin/bash
# send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
curl -s "$1" -X POST -d @"$2" -H "Content-Type: application/json"
