from httplib2 import Http
from json import dumps
import json

with open('Cred','r') as f:
    con = json.load(f)

def main():
    url = con['Chat']
    bot_message = {
        'text': 'Hello World'}

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()
