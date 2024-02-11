from ncclient import manager
import xmltodict
import json


def editLoopback():
    device_info = {
    "host":"sandbox-iosxe-latest-1.cisco.com",
    "port":830,
    "username":"admin",
    "password":"C1sco12345",
    "device_params":{'name': 'iosxe'}
}
    LOOPBACK = '153'
    DESCRIPTION = 'TEST CREATED BY NETMAN WILLY'
    IP = '153.153.153.153'
    SUBNET = '255.255.255.255'

    PAYLOAD = {
            "config": {
                "@xmlns": "urn:ietf:params:xml:ns:netconf:base:1.0",
                "@xmlns:nc": "urn:ietf:params:xml:ns:netconf:base:1.0",
                "native": {
                "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XE-native",
                "interface": {
                    "Loopback": {
                    "name": "153",
                    "description": "TEST CREATED BY NETMAN WILLY EDITED",
                    "ip": {
                        "address": {
                        "primary": {
                            "address": "153.153.153.153",
                            "mask": "255.255.255.255"
                        }
                        }
                    },
                    }
                }
                }
            }
            }
    
    '''<config><xmlns>urn:ietf:params:xml:ns:netconf:base:1.0</xmlns>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <interface><nc:operation>delete</nc:operation>
                    <Loopback>
                    <name>153</name>
                    <description>TEST CREATED BY NETMAN WILLY</description>
                    <ip>
                        <address>
                            <primary>
                                <address>153.153.153.153</address>
                                <mask>255.255.255.255</mask>
                            </primary>
                        </address>
                    </ip>
                    </Loopback>
                </interface>
            </native>
        </config>'''
    

    XMLPAYLOAD = xmltodict.unparse(PAYLOAD)
    print(XMLPAYLOAD)

    with manager.connect(**device_info) as device:
        OUTPUT = device.edit_config(target ='running', config=XMLPAYLOAD)
        return OUTPUT




if __name__ == '__main__':
    print(editLoopback())