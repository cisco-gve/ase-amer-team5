import requests

url = "https://198.18.134.173/api/3.3/monitoring/overview"

headers = {
    'content-type': "application/json",
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'cache-control': "no-cache",
    'token': "b84be681-44c6-04b4-f765-a43e287b13ea"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
