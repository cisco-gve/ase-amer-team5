import requests

url = "https://198.18.134.173/api/3.3/management/controllers"

headers = {
    'content-type': "application/json",
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'cache-control': "no-cache",
    'token': "af3b3b42-04e8-0647-263d-08d89a7517dc"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
