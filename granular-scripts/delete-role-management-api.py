import requests

url = "https://198.18.134.173/api/3.3/management/roles"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'token': "93305e65-9e97-4747-44db-2b305939caac"
    }

response = requests.request("DELETE", url, headers=headers)

print(response.text)
