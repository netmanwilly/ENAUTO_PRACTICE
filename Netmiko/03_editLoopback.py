import netmiko

def editLoopback():
    device = {
    "device_type":"cisco_xe",
    "host":"sandbox-iosxe-latest-1.cisco.com",
    "username":"admin",
    "password": "C1sco12345"
}
    
    CONNECTION = netmiko.ConnectHandler(**device)
    COMMAND = ['interface lo153', 'description Netmiko test EDITED by NETMANWILLY']

    OUTPUT = CONNECTION.send_config_set(COMMAND)
    OUTPUT += CONNECTION.send_command('show run | s Loopback153')

    return OUTPUT


if __name__ == '__main__':
    print(editLoopback())