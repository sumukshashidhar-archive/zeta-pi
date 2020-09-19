import json
import requests
import time

def getToken():
    return json.loads(
        requests.post(
            url = "http://40.76.37.214:3000/login",
            data = {
                "username": "nn1vh8Uxqcn5F6TmSh",
                "password": "nn1vh8Uxqcn5F6TmSh"
            }
        ).text
    )["token"]

response = requests.post(
    url = "http://40.76.37.214:80/api/upload/image",
    data = {
        "token": token
    },
    files = {
        "image": open('test.png','rb')
    }
)

print(response)