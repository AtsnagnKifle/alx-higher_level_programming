#!/bin/bash
# takes in a URL and displays all HTTP methods
curl -sI -X OPTIONS "$1" | grep Allow | cut -b 8-
