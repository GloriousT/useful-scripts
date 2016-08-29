#!/usr/bin/python3

import requests
import sys

data = dict(
    Domain='mail.ru',
    Login='empty',
    Password='empty'
)

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive'
}


def main(login, password):
    data["Login"] = login
    data["Password"] = password

    for item in data.items():
        print(item)
    response = requests.post("https://auth.mail.ru/cgi-bin/auth?from=splash", data=data, headers=headers)
    for c in response.headers.items():
        print(c)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
