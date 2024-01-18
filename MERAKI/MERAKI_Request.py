import requests
import json


class Meraki:
    def __init__(self, host, token, verify=True):
        self.host = host
        self.verify = verify
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        
        if not self.verify:
            requests.packages.urllib3.disable_warnings()
        

    def get(self, URI):
        RESPONSE = requests.get(self.host + URI, headers=self.headers, verify=False)
        return RESPONSE.json()


if __name__ == '__main__':
    meraki = Meraki('https://api.meraki.com/api/v1', '6bec40cf957de430a6f1f2baa056b99a4fac9ea0')
    print(json.dumps(meraki.get('/organizations'), indent=2))