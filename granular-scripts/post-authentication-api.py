import requests

url = "https://198.18.134.173/api/3.3/login"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'token': "60b1691f-fcc5-34dc-c385-41cf77d41a13"
    }

response = requests.request("POST", url, headers=headers)

print(response.text)
