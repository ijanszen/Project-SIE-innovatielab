import time
import requests
# //Include the Beebotte SDK for Python
from beebotte import *

headers = {
    'Accept': "application/json",
    'X-Access-Token': "NTQzYzcyN2E5YjQzZmUwNWUxYWMxNGEyNjc5NjIyMjAyOTIwYzllZTAxZjZkNzM2N2Q5NWM1ZTg0MDEwZWRjNw==",
    'Cache-Control': "no-cache"
    }

url = "https://developer.lametric.com/api/v1/dev/widget/update/com.lametric.953158e991adfff104e517cb87d362bd/2"

# Tokeninfo
_hostname   = 'api.beebotte.com'
_token      = 'token_zp8cDd365areasf1'
records = ''

bbt = BBT(token = _token, hostname = _hostname)


def mqtt_read(resource,lim):
    ## Read data
    records = bbt.read('NetAtmo', str(resource), limit = int(lim), source = 'raw')
    return records

a = ["Pressure","mbar"]
b = ["Co2","ppm"]
c = ["Humidity","%"]
d = ["Noise","dB"]
e = ["Temperature","C"]
f = ["WiFi_stat","%"]

list1 = [a, b, c, d, e, f]
length = len(list1)

while True:
    for i in range(length):
        d = mqtt_read(list1[i][0],1)[0]['data']
        p = str(list1[i][0] + " " + str(d) + " " + list1[i][1])
        payload = "{\n \"frames\": [\n {\n \"text\": \"" + p + "\",\n \"icon\": \"i28070\",\n \"index\": 0\n }\n ]\n}"
        try:
            response = requests.request("POST", url,  headers=headers, data=payload)
            print(response)
        except:
            print(p)
        time.sleep(10)