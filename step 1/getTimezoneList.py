import requests

url = "https://198.18.134.173/api/3.3/data/getTimezoneList"

headers = {
    'content-type': "application/json",
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'cache-control': "no-cache",
    'postman-token': "6773ce5b-e695-23a4-4835-f0d74e3d7f27"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
