from netmiko import ConnectHandler
from Netmiko_helper_functions.get_device import get_object

def connect():
    device = get_object()
    connection = ConnectHandler(**device)
    print(f'Connecting to device {device['host']}')
    return connection


if __name__ == "__main__":
    test = connect()
    print(test.find_prompt())
