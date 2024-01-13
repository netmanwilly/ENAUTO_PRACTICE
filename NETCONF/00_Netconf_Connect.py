#CONNECT TO DEVICE USING NETCONF AND PRINT RUNNING CONFIG IN XML FORMAT
from ncclient import manager
device = {
    "host":"sandbox-iosxe-latest-1.cisco.com",
    "port":830,
    "username":"admin",
    "password":"C1sco12345",
    "device_params":{'name': 'iosxe'}
}

with manager.connect(**device) as test:
    config = test.get_config(source='running').data_xml
    print(config)