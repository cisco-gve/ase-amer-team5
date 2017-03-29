import requests

url = "https://198.18.134.173/api/3.3/management/tenants"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'token': "2a90b03d-ab8c-1bae-9b07-efa84032845d"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
