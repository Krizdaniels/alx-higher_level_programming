#!/bin/bash
# It takes in URL, sends request to the URL, displays size of body response
curl -sX GET $1 -L
