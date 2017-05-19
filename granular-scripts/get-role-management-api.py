import requests

url = "https://198.18.134.173/api/3.3/management/roles"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'token': "bcc94b47-0685-5b66-c948-6c1668e4690c"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
