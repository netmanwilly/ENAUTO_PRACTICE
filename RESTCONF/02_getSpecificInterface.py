#Get specific interface config using RESTCONF on NXOS device\

import requests
import json
import xmltodict

def getSpecificInterface():
    BASE_URI = 'https://devnetsandboxiosxe.cisco.com'
    USER = 'admin'
    PASS = 'C1sco12345'
    RESTCONF = 443
    API = '/restconf/data/ietf-interfaces:interfaces'

    HEADERS = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }

    RESPONSE = requests.get(BASE_URI + API, auth=(USER, PASS), headers=HEADERS, verify=False)
    RESPONSE.raise_for_status
    if RESPONSE.status_code == 204:
        return f'NOTHING TO SEE HERE: {RESPONSE.status_code}'
    #OUTPUT =  xmltodict.parse(RESPONSE.text, process_namespaces=True)
    print(RESPONSE.status_code)
    return RESPONSE.text



if __name__ == '__main__':
    print(getSpecificInterface())


