import netmiko
import json
from Netmiko_helper_functions.connect_helper import connect

device = connect()
show_command = device.send_command("show ip arp")
print(show_command)

