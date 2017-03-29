import requests

url = "http://example.com/api/3.3/scripts/js/execute"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'token': "62e64c65-1c09-5cbd-0c65-cf925d3d520a"
    }

response = requests.request("POST", url, headers=headers)

print(response.text)
