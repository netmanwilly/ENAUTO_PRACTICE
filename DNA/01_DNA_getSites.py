import json
from pprint import pprint
import requests
requests.packages.urllib3.disable_warnings()


def getToken():
    BASE_URI = "https://sandboxdnac2.cisco.com"
    USER = "devnetuser"
    PASS = "Cisco123!"
    AUTH_URI = "/dna/system/api/v1/auth/token"

    HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': ''
    }

    RESPONSE = requests.post(BASE_URI + AUTH_URI, auth=(USER, PASS), headers=HEADERS, verify=False)
    RESPONSE.raise_for_status
    if RESPONSE.status_code != 200:
        print(f'Error! {RESPONSE.status_code}')
    else:
        output = RESPONSE.json()
        return output['Token']


def getSite(token: str):
    BASE_URI = "https://sandboxdnac2.cisco.com"
    SITE_URI = '/dna/intent/api/v1/site'
    HEADERS = {
    "X-Auth-Token": token,
    "Content-Type": "application/json",
    "Accept": "application/json"
    }
    
    RESPONSE = requests.get(BASE_URI + SITE_URI, headers=HEADERS, verify=False)
    RESPONSE.raise_for_status
    if RESPONSE.status_code != 200:
        return RESPONSE.status_code
    else:
        return RESPONSE.json()


if __name__ == '__main__':
    token = getToken()
    #print(type(token))
    pprint(getSite(token), indent= 4)