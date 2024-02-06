#Test RESTCONF on NX-OS with better experience with requests module
import requests
import json
import xmltodict

def getCapabilities():
    BASE_URI = 'https://sbx-nxos-mgmt.cisco.com'
    USER = 'admin'
    PASS = 'Admin_1234!'
    RESTCONF = 443
    API = '/restconf/data/Cisco-NX-OS-device:System/'

    HEADERS = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }

    RESPONSE = requests.get(BASE_URI + API, auth=(USER, PASS), headers=HEADERS, verify=False)
    RESPONSE.raise_for_status
    print(f'HERES YOUR STATUS CODE: {RESPONSE.status_code}')
    OUTPUT = xmltodict.parse(RESPONSE.text)
    return json.dumps(OUTPUT, indent=2)



if __name__ == '__main__':
    NXOS_CONFIG = getCapabilities()
    with open('NXOS-CONFIG.json', 'w') as file:
        file.write(NXOS_CONFIG)
    print(type(getCapabilities()))

