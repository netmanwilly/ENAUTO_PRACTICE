import requests
import json
import xmltodict

requests.packages.urllib3.disable_warnings()
def Connect():
    BASE_URI = 'https://devnetsandboxiosxe.cisco.com'
    USER = 'admin'
    PASS = 'C1sco12345'
    API = '/restconf/data/Cisco-IOS-XE-native:native/'
    
    HEADERS = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }

    RESPONSE = requests.get(BASE_URI + API, auth=(USER, PASS), headers=HEADERS, verify=False)
    RESPONSE.raise_for_status
    if RESPONSE.status_code == 204:
        return 'NOTHING TO SEE HERE' 
    return RESPONSE


if __name__ == '__main__':
    print(Connect())