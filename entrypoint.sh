#!/bin/bash

if ! [[ "$BASE_URL" == "" ]] || ! [[ "$AUTH_LOGIN" == "" ]] || ! [[ "$AUTH_PASS" == "" ]]; then
  pipenv run python3 \
    -m pytest \
    -s tests \
    --alluredir=allure_res \
    -v

else
  echo "No way Jose! You haven't specify required environment variables! Come back when you ready"
  exit 1
fi
