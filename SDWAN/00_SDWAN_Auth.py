import requests
import json

#In order to authenticate, send POST request to resource with user name and password in the HTTP Body of the request

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

if __name__ == '__main__':
    print(SDWAN_Auth())