import requests
import json

requests.packages.urllib3.disable_warnings()

def main():
    BASE_URI = "https://sandboxdnac2.cisco.com"
    USER = "devnetuser"
    PASS = "Cisco123!"
    AUTH_URI = "/dna/system/api/v1/auth/token"

    HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': ''
        #'Authorization': 'Basic devnetuser:Cisco123!'
    }

    RESPONSE = requests.post(BASE_URI + AUTH_URI, auth=(USER, PASS), headers=HEADERS, verify=False)
    RESPONSE.raise_for_status
    #CHECKS IF RESOURCE IS NOT FOUND
    if RESPONSE.status_code != 204:
        output = RESPONSE.text
        print(output)
    else:
        print("RESOURCE NOT FOUND")


if __name__ == "__main__":
    main()