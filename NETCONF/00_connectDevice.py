#Intial connect and return output of running config in json

from ncclient import manager
import xmltodict
import json


def connectDevice():
    device = {
    "host":"sandbox-iosxe-latest-1.cisco.com",
    "port":830,
    "username":"admin",
    "password":"C1sco12345",
    "device_params":{'name': 'iosxe'}
}
    
    with manager.connect(**device) as device:
        SCHEMA = device.server_capabilities
        for X in SCHEMA:
            print(X)
        return SCHEMA

    #with manager.connect(**device) as device:
    #    CONFIG = device.get_config('running').data_xml
    #    OUTPUT = xmltodict.parse(CONFIG)
    #    return json.dumps(OUTPUT, indent=2)
    





if __name__ == '__main__':
    print(connectDevice())