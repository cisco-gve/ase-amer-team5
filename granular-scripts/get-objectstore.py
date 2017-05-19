import requests

url = "https://198.18.134.173/api/3.3/objectstore"

headers = {
    'content-type': "application/json",
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'cache-control': "no-cache",
    'token': "6865907c-a78c-41cf-638e-4c1fc528ea25"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
