import json

#Created script for easier object management to access for testing
device = {
    "device_type":"cisco_xe",
    "host":"sandbox-iosxe-latest-1.cisco.com",
    "username":"admin",
    "password": "C1sco12345"
}

def get_object():
    return device



if __name__ == "__main__":
    print(get_object())