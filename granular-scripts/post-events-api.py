import requests

url = "https://198.18.134.173/api/3.3/events"

headers = {
    'content-type': "application/json",
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'cache-control': "no-cache",
    'token': "60a8cc51-1b76-3207-d354-24b744ec4125"
    }

response = requests.request("POST", url, headers=headers)

print(response.text)
