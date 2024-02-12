import requests
import json
import xmltodict

requests.packages.urllib3.disable_warnings()
def createLoopback():
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
            "Loopback": [{
                "name": 153,
                "description": "RESTCONF TEST CREATED BY NETMAN WILLY",
                "ip": {
                    "address": {
                        "primary": {
                            "address": "153.153.153.153",
                            "mask": "255.255.255.255"
                        }
                    }
                }
            }]
        }
    }

    JSONPAYLOAD = json.dumps(PAYLOAD)
        

    RESPONSE = requests.put(BASE_URI + API, auth=(USER, PASS), headers=HEADERS, data=JSONPAYLOAD, verify=False)
    RESPONSE.raise_for_status
    if RESPONSE.status_code == 204:
        return 'NOTHING TO SEE HERE' 
    if RESPONSE.status_code > 400:
        return f'ERROR: {RESPONSE.status_code}'
    return RESPONSE.json()


if __name__ == '__main__':
    print(createLoopback())