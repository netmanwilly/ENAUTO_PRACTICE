#create loopback interface 
from ncclient import manager
import xmltodict
import json
from pprint import pprint

#KEY NOTE FOR FILTER, YOU NEED TO SPECIFY WHAT YANG MODEL YOU ARE USING 

def getLoopback():
    device_info = {
    "host":"sandbox-iosxe-latest-1.cisco.com",
    "port":830,
    "username":"admin",
    "password":"C1sco12345",
    "device_params":{'name': 'iosxe'}
}
    FILTER = '''
  <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
             <Loopback>
             </Loopback>
         </interface>
    </native>
  </filter>
'''

    with manager.connect(**device_info) as device:
        RESPONSE = device.get_config('running', FILTER).data_xml
        OUTPUT = xmltodict.parse(RESPONSE)
        TOTAL_LOOPBACK = OUTPUT['data']['native']['interface']['Loopback']
        print(f'THERE ARE {len(TOTAL_LOOPBACK)} CURRENTLY CONFIGURED LOOPBACKS ON {device_info['host']}. THE LIST IS AS FOLLOWS:')
        for X in TOTAL_LOOPBACK:
            print(f'   - {X['name']}')

        return json.dumps(OUTPUT, indent=2)





if __name__ == '__main__':
    print(getLoopback())