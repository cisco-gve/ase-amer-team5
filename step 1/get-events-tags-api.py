import requests

url = "https://198.18.134.173/api/3.3/events/tags"

headers = {
    'content-type': "application/json",
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'cache-control': "no-cache",
    'token': "8b50032b-96b5-c90e-2818-9246f3ef80ac"
    }

response = requests.request("PUT", url, headers=headers)

print(response.text)
