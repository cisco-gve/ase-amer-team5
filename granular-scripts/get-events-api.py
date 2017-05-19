import requests

url = "https://198.18.134.173/api/3.3/events"

headers = {
    'content-type': "application/json",
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'cache-control': "no-cache",
    'token': "f3165de6-5f79-9f2f-f96b-28a61f3ce674"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
