#Get specific part of config using filter for specific data
from ncclient import manager
device = {
    "host":"sandbox-iosxe-latest-1.cisco.com",
    "port":830,
    "username":"admin",
    "password":"C1sco12345",
    "device_params":{'name': 'iosxe'}
}
#####create filter to get specific interface data
FILTER = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <GigabitEthernet>
            <name>1</name>
                <ip>
                    <address>
                        <primary>
                            <address></address>
                        </primary>
                    </address>
                </ip>
            </GigabitEthernet>
        </interface>
    </native>
</filter>
"""
with manager.connect(**device) as test:
    config = test.get_config('running', FILTER).data_xml
    print(config)