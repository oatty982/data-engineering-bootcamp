#!/bin/bash

API_KEY='$2b$10$WGheK77igyrUGVA2hNgky./oe6dZBWJoOnw1SvmZv932Cq3fegWpG'
COLLECTION_ID='64cdf95eb89b1e2299cbae09'

curl -XPOST \
    -H "Content-type: application/json" \
    -H "X-Master-Key: $API_KEY" \
    -H "X-Collection-Id: $COLLECTION_ID" \
    -d @dogs.json \
    "https://api.jsonbin.io/v3/b"
