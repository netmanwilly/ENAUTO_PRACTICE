#Get SDWAN device inventory
#Requests are made using HTTP GET OPERATION
#GET https://{vmanage-ip-address}/dataservice/device
#Content-Type: application/json

import requests
import json

requests.packages.urllib3.disable_warnings()

def SDWAN_Auth():
    BASE_URI = 'https://sandbox-sdwan-2.cisco.com'
    USER = 'devnetuser'
    PASS = 'RG!_Yw919_83'

    HEADERS = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    PAYLOAD = f'j_username={USER}&j_password={PASS}'

    RESPONSE = requests.post(BASE_URI + '/j_security_check', headers=HEADERS, data=PAYLOAD, verify=False)
    RESPONSE.raise_for_status
    if RESPONSE.status_code != 200:
        raise ValueError("ERROR")
    print(f'SDWAN Basic Auth Status Code: {RESPONSE.status_code}')
    
    COOKIE = RESPONSE.headers['Set-Cookie'].split(';')
    return COOKIE[0]

def getDeviceInv():
    BASE_URI = 'https://sandbox-sdwan-2.cisco.com'
    API = '/dataservice/device'

    HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': SDWAN_Auth()
    }

    RESPONSE = requests.get(BASE_URI + API, headers=HEADERS, verify=False)
    RESPONSE.raise_for_status
    if RESPONSE.status_code != 200:
        raise ValueError("UH-OH")
    
    #Returns entire response
    #specify key ['data'] for just device info
    return RESPONSE.json()

print(json.dumps(getDeviceInv(), indent=2))