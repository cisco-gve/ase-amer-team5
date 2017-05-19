import requests

url = "https://198.18.134.173/api/3.3/management/roles"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'token': "b6e18ef3-7c29-a49c-3857-4fd14aecf5ca"
    }

response = requests.request("POST", url, headers=headers)

print(response.text)
