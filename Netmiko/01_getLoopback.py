import netmiko

def getLoopback():
    device = {
    "device_type":"cisco_xe",
    "host":"sandbox-iosxe-latest-1.cisco.com",
    "username":"admin",
    "password": "C1sco12345"
}
    IS_THERE = False
    LOOPBACK = 'Loopback153'
    
    CONNECTION = netmiko.ConnectHandler(**device)
    COMMAND = 'show run | sec Loopback153'
    CHECK = CONNECTION.send_command('show ip int brief', use_textfsm = True)
    for X in CHECK:
        if X['interface'] == LOOPBACK:
            IS_THERE = True
    
    if IS_THERE is True:
        return CONNECTION.send_command(COMMAND, use_textfsm=True)
    else:
        return 'Loopback does not exist'
    




if __name__ == '__main__':
    print(getLoopback())