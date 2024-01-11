import netmiko

###########################################
# Create device dictionary containing details about device
# Connect to device and verify if theres a prompt
########################################
device = {
    "device_type":"cisco_xe",
    "host":"sandbox-iosxe-latest-1.cisco.com",
    "username":"admin",
    "password": "C1sco12345"
}
connect = netmiko.ConnectHandler(**device)
print(connect.find_prompt())