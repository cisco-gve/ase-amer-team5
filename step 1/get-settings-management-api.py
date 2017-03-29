import requests

url = "http://example.com/api/3.3/management/getenv"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'token': "4d6b3999-1c25-8e97-92ce-dcdfb5023248"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
