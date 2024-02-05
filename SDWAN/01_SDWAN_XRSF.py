#For most future POST operations, a XRSF Token must be present to make requests

import requests
import json

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


#RETURNS STRING THAT CONTAINS XRSF TOKEN
#TOKEN NEEDS TO BE ADDED TO FUTURE POST OPERATION REQUESTS ALONG WITH JSESSION COOKIE
#{
#'Cookie': {jsessionId}
#'X-XRSF-TOKEN'': {TOKEN}
#}
def SDWAN_XRSF():
    JSESSION = SDWAN_Auth()
    BASE_URI ='https://sandbox-sdwan-2.cisco.com'
    API = '/dataservice/client/token'

    HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': JSESSION
    }

    RESPONSE = requests.get(BASE_URI + API, headers=HEADERS, verify=False)
    RESPONSE.raise_for_status
    if RESPONSE.status_code != 200:
        raise ValueError(f'ERROR: {RESPONSE.status_code}')
    
    return RESPONSE.text


if __name__ == '__main__':
    print(SDWAN_XRSF())