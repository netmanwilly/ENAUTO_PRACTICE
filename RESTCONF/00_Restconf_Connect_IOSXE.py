import requests
requests.packages.urllib3.disable_warnings()
host = "sandbox-iosxe-latest-1.cisco.com"
user = "admin"
password = "C1sco12345"

def main():

    # url string to issue GET request
    url = "https://{h}/restconf/data/ietf-interfaces:interfaces".format(h=host)

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    
    response = requests.get(url, auth=(user, password), headers=headers, verify=False)
    print(response.text)
    print(type(response))

if __name__ == "__main__":
    main()