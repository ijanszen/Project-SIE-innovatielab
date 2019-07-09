import requests

url = "http://192.168.3.192:16021/api/v1/8waBfTkcAQAFDFP1CRoaR6u2pg8ScVio/effects"

payload = '{"write":{"animData":"7 139 2 255 255 255 1 10 0 255 0 1 15 234 2 255 255 255 1 10 0 255 0 1 20 201 2 255 255 255 1 10 0 255 0 1 25 117 2 255 255 255 1 10 0 255 0 1 30 200 2 255 255 255 0 10 0 255 0 0 35 104 2 255 255 255 0 10 0 255 0 0 40 243 2 255 255 255 0 10 0 255 0 0 45","animType":"custom","command":"display","loop":false}}'

response = requests.request("PUT", url, data=payload)

print(response.text)