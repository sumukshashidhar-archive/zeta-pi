import json
import requests
import time
import jw

def getToken(name,pw):
    return json.loads(
        requests.post(
            url = "http://40.76.37.214:3000/login",
            data = {
                "username": name,
                "password": pw
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

def register(name,pw,role,creation_pw):
    r = requests.post(
        url = "http://40.76.37.214:3000/register",
        data = {
            "username":name,
            "password":role,
            "role":role,
            "creation_password": creation_pw
            }        
        )
        print(r.text)