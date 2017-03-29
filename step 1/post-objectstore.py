import requests

url = "https://198.18.134.173/api/3.3/objectstore"

headers = {
    'content-type': "application/json",
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'cache-control': "no-cache",
    'token': "2042fa6a-abbe-7f2d-2d1c-ba590097ccde"
    }

response = requests.request("POST", url, headers=headers)

print(response.text)
