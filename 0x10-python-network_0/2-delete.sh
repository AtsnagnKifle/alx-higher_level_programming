#!/bin/bash
# sends a DELETE request to the URL passed as the first argument
curl -sb /dev/null -X DELETE "$1" 
