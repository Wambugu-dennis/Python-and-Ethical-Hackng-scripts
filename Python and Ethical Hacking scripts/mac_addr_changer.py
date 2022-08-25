# created by Wambugu Dennis
# 25-08-2022


import subprocess
import optparse
import re


# modeled options to take arguments from commands with help option
# capture input from user -option and arguments
# check if all req options and arguments are supplied in the commands
# return options if check succeeds
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify an new MAC Address, use --help for more info.")
    return options


# change the mac address of interface by supplying -options and arguments values returned above
def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


# read mac address from ifconfig result using regular expressions
# python 3 using byte data as string to mitigate error
# returns string value to be parsed as current mac
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not get the MAC Address.")
    print(mac_address_search_result.group(0))


options = get_arguments()

# get current mac from function
current_mac = get_current_mac(options.interface)
print("[+] Current MAC Address > " + str(current_mac))

# call function to change mac address
change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)  # check for changed mac address, should be new mac address
if current_mac == options.new_mac:
    print("[+] MAC Address successfully changed to " + current_mac)  # display current mac address supplied
else:
    print("[-] MAC Address not changed.")