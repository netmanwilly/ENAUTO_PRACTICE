import requests
import json
requests.packages.urllib3.disable_warnings()


def getToken():
    HOST = "https://sandboxdnac2.cisco.com"
    USER = 'devnetuser'
    PASS = 'Cisco123!'
    API = '/dna/system/api/v1/auth/token'
    HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization':''
    }
    RESPONSE = requests.post(HOST + API, auth=(USER, PASS), headers=HEADERS, verify=False)
    RESPONSE.raise_for_status
    if RESPONSE.status_code != 200:
        raise ValueError(f'ERROR {RESPONSE.status_code}')
    OUTPUT = RESPONSE.json()
    return OUTPUT['Token']


def getSiteCount():
    API_URI = '/dna/intent/api/v1/site/count'
    BASE_URI = 'https://sandboxdnac2.cisco.com'
    HEADERS = {
        'X-Auth-Token': getToken(),
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    RESPONSE = requests.get(BASE_URI + API_URI, headers=HEADERS, verify=False)
    RESPONSE.raise_for_status
    if RESPONSE.status_code != 200:
        raise ValueError(RESPONSE.status_code)
    return RESPONSE.json()

print(json.dumps(getSiteCount(), indent=2))