# import requests
# import json
#
# url = "http://127.0.0.1:8001/api/api/4/"
# payload = json.dumps({
#     "city": "Craiova3",
#     "country": "Romania"
# })
# headers = {
#     "Content-Type": "application/json"
# }
#
# response = requests.request("DELETE", url, headers=headers, data=payload)
# print(response.json())

import requests

url = "https://v6.exchangerate-api.com/v6/2e21dd1971f4eeb96e61c4e8/latest/RON"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json()["conversion_rates"]["EUR"])
