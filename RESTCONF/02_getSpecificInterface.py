#Get specific interface config using RESTCONF on NXOS device\

import requests
import json
import xmltodict

def getSpecificInterface():
    BASE_URI = 'https://sbx-nxos-mgmt.cisco.com'
    USER = 'admin'
    PASS = 'Admin_1234!'
    RESTCONF = 443
    API = '/restconf/data/Cisco-NX-OS-device:/System/intf-items/phys-items/'

    HEADERS = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }

    RESPONSE = requests.get(BASE_URI + API, auth=(USER, PASS), headers=HEADERS, verify=False)
    RESPONSE.raise_for_status
    if RESPONSE.status_code == 204:
        return f'NOTHING TO SEE HERE: {RESPONSE.status_code}'
    OUTPUT =  xmltodict.parse(RESPONSE.text, process_namespaces=True)
    print(RESPONSE.status_code)
    return json.dumps(OUTPUT, indent=2)



if __name__ == '__main__':
    print(getSpecificInterface())


