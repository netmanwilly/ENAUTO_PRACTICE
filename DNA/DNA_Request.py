#Lightweight SDK to simplify getting Auth-Token and initialize requests using OOP principles 

import json
import requests


class DNA_Request:

    def __init__(self, host, user, password, verify=True):
        self.host = host
        self.verify = verify
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        if not verify:
            requests.packages.urllib3.disable_warnings()
        
        AUTH_URI = "/dna/system/api/v1/auth/token"
        RESPONSE = requests.post(self.host + AUTH_URI, auth=(user, password), headers=self.headers, verify=self.verify)
        RESPONSE.raise_for_status
        self.headers['X-Auth-Token'] = RESPONSE.json()['Token']

    def __str__(self) -> str:
        string = f'HOST: {self.host}\nHEADERS: {json.dumps(self.headers, indent=2)}'
        return string
