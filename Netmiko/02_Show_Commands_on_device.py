import netmiko
import json
from Netmiko_helper_functions.connect_helper import connect

device = connect()
print(device.find_prompt())

