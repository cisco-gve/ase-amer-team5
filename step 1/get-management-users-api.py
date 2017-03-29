import requests

url = "https://192.18.134/173/api/3.3/management/users"

payload = ""
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "08ba8744-0f97-07e9-2743-42d9d6de8fa5"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)