import json
import requests
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


def getSite():
    BASE_URI = "https://sandboxdnac2.cisco.com"
    SITE_URI = '/dna/intent/api/v1/site'
    HEADERS = {
    "X-Auth-Token": getToken(),
    "Content-Type": "application/json",
    "Accept": "application/json"
    }
    
    RESPONSE = requests.get(BASE_URI + SITE_URI, headers=HEADERS, verify=False)
    RESPONSE.raise_for_status
    if RESPONSE.status_code != 200:
        raise ValueError(RESPONSE.status_code) 
    OUTPUT = RESPONSE.json()
    #JAN 31 2024
    #SITE COUNT IS CURRENTLY AT 16 SO RETURN LAST SITE TO TEST MEMBERSHIP
    return OUTPUT['response'][15]['id']

def getSiteMembership():
    siteId = getSite()
    BASE_URI = "https://sandboxdnac2.cisco.com"
    SITE_URI = f'/dna/intent/api/v1/membership/{siteId}'
    HEADERS = {
    "X-Auth-Token": getToken(),
    "Content-Type": "application/json",
    "Accept": "application/json"
    }
    
    RESPONSE = requests.get(BASE_URI + SITE_URI, headers=HEADERS, verify=False)
    RESPONSE.raise_for_status
    if RESPONSE.status_code != 200:
        raise ValueError(RESPONSE.status_code) 
    return RESPONSE.json()
 

if __name__ == '__main__':
    token = getToken()
    #print(type(token))
    print(json.dumps(getSiteMembership(), indent=2))