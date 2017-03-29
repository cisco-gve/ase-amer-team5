import requests

url = "https://198.18.134.173/api/3.3/monitoring/states"

headers = {
    'content-type': "application/json",
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'cache-control': "no-cache",
    'token': "d12efbb4-653e-590c-ee85-8093f2a44788"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
