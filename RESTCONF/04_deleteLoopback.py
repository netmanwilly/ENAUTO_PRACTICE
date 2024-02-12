import requests
import json

requests.packages.urllib3.disable_warnings()

def deleteLoopback():
    BASE_URI = 'https://devnetsandboxiosxe.cisco.com'
    USER = 'admin'
    PASS = 'C1sco12345'
    API = '/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=153'
    
    HEADERS = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }

    PAYLOAD = {
        "Cisco-IOS-XE-native:Loopback": {
            "name": 153,
            "description": "RESTCONF TEST CREATED BY NETMAN WILLY EDITED",
            "ip": {
                "address": {
                    "primary": {
                        "address": "153.153.153.153",
                        "mask": "255.255.255.255"
                    }
                }
            }
        }
    }

    JSONPAYLOAD = json.dumps(PAYLOAD)
        
    RESPONSE = requests.delete(BASE_URI + API, auth=(USER, PASS), headers=HEADERS, data=JSONPAYLOAD, verify=False)
    
    try:
        RESPONSE.raise_for_status()
    except requests.exceptions.HTTPError as err:
        return f"ERROR: {err}"

    if RESPONSE.status_code == 204:
        return 'Loopback interface removed successfully.'
        
    else:
        return f'Unexpected response: {RESPONSE.status_code}'

if __name__ == '__main__':
    print(deleteLoopback())
