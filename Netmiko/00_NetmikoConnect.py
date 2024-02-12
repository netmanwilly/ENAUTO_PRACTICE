import netmiko

def Connect():
    device = {
    "device_type":"cisco_xe",
    "host":"sandbox-iosxe-latest-1.cisco.com",
    "username":"admin",
    "password": "C1sco12345"
}

    CONNECTION = netmiko.ConnectHandler(**device)

    return CONNECTION.find_prompt()


if __name__ == '__main__':
    print(Connect())