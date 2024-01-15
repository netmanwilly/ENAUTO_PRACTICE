import requests
import json
requests.packages.urllib3.disable_warnings()
host = "sbx-nxos-mgmt.cisco.com"
user = "admin"
password = "Admin_1234!"

def main():

    # url string to issue GET request
    url = "https://{h}/restconf/data/".format(h=host)

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    
    response = requests.get(url, auth=(user, password), headers=headers, verify=False)
    response.raise_for_status
    if response.status_code != 204:
        print(response)
    else:
        print(f"NOTHING HERE MAN THE CODE IS {response.status_code}")

if __name__ == "__main__":
    main()