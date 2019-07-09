import requests
import time
from beebotte import *

# Tokeninfo
_hostname   = 'api.beebotte.com'
_token      = 'token_zp8cDd365areasf1'

bbt = BBT(token = _token, hostname = _hostname)

# this function gets the acces token by logging in.
# this is because nettamo tokens are temporary
def gettoken():
    global access_token
    global refresh_token
    payload = {'grant_type': 'password',
            'username': "alex.jongman@hu.nl",
            'password': "#HBO-ict",
            'client_id':"5c98c95558b0f415008b53e4",
            'client_secret': "Rs5jnwgmpiOXW5wcN572ghgevrnnmac",
            'scope': 'read_homecoach'}
    try:
        response = requests.post("https://api.netatmo.com/oauth2/token", data=payload)
        response.raise_for_status()
        access_token=response.json()["access_token"]
        refresh_token=response.json()["refresh_token"]
        scope=response.json()["scope"]
    except requests.exceptions.HTTPError as error:
        print(error.response.status_code, error.response.text)

# this function gets data from the netatmo using the api and the acces token and puts it in the var data
def getdata():
    gettoken()
    global data
    params = {
        'access_token': access_token,
        'device_id': '70:ee:50:25:a7:ba'
    }

    try:
        response = requests.post("https://api.netatmo.com/api/gethomecoachsdata", params=params)
        response.raise_for_status()
        data = response.json()["body"]
    except requests.exceptions.HTTPError as error:
        print(error.response.status_code, error.response.text)

#this function takes the data and from the json data file and formats it.
# after the formated data will be send to beebotte
def send():
    #parse json
    ab_pressure = data['devices'][0]['dashboard_data']['AbsolutePressure']
    co2 = data['devices'][0]['dashboard_data']['CO2']
    humidity = data['devices'][0]['dashboard_data']['Humidity']
    noise = data['devices'][0]['dashboard_data']['Noise']
    pressure = data['devices'][0]['dashboard_data']['Pressure']
    temp = data['devices'][0]['dashboard_data']['Temperature']
    health_idx = data['devices'][0]['dashboard_data']['health_idx']
    max_temp = data['devices'][0]['dashboard_data']['max_temp']
    min_temp = data['devices'][0]['dashboard_data']['min_temp']
    wifi_status = data['devices'][0]['wifi_status']
    # Write bulk to Beebotte
    bbt.writeBulk("NetAtmo", [
        {"resource": "Absolute_pres", "data": ab_pressure},
        {"resource": "Co2", "data": co2},
        {"resource": "Humidity", "data": humidity},
        {"resource": "Noise", "data": noise},
        {"resource": "Pressure", "data": pressure},
        {"resource": "Temperature", "data": temp},
        {"resource": "Healt_idx", "data": health_idx},
        {"resource": "Max_temp", "data": max_temp},
        {"resource": "Min_temp", "data": min_temp},
        {"resource": "WiFi_stat", "data": wifi_status}        
    ])

# this will send the data every 30 seconds
while True:
    getdata()
    send()
    print("data send")
    time.sleep(30)
    