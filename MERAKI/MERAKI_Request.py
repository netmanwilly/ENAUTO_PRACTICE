import requests
import json


class Meraki:
    def __init__(self, host, token, verify=False):
        self.host = host
        self.verify = verify
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        
        if self.verify:
            requests.packages.urllib3.disable_warnings()
        

    def get(self, URI):
        RESPONSE = requests.get(self.host + URI, headers=self.headers, verify=False)
        RESPONSE.raise_for_status
        if RESPONSE.status_code != 200:
            return f'ERROR: {RESPONSE.status_code}'
        else:
            return RESPONSE.json()
        
    def put(self, URI, payload):
        RESPONSE = requests.request('PUT', self.host + URI, headers=self.headers, data=payload, verify=False)
        print(payload)
        RESPONSE.raise_for_status
        if RESPONSE.status_code != 200:
            return f'ERROR: {RESPONSE.status_code}'
        else:
            return RESPONSE.json()


if __name__ == '__main__':
    meraki = Meraki('https://n149.meraki.com/api/v1', 'ccb3f4e44b2d75881d1471fcfa9a823149e69a9c', False)
    print(json.dumps(meraki.get('/organizations/549236/networks'), indent=2))

    