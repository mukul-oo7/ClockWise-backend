import requests
import json

url = "http://localhost:8000/auth/register/"


headers = {
    "Content-Type": "application/json"
}

for i in range(10):

    payload = {
    "name":"student"+str(i),
    "id":i,
    "email_id":"student"+str(i)+"@gmail.com",
    "password":"student"+str(i),
    "department":"CSE",
    "cat":"Student"
    }

    json_payload = json.dumps(payload)

    response = requests.post(url, data=json_payload, headers=headers)

    if response.status_code == 200:
        print(str(i)+" POST request successful!")
    else:
        print(str(i)+f" POST request failed with status code {response.status_code}:")
        print(response.text)
