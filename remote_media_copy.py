import os
import subprocess
import time
import sys
from shutil import disk_usage

print("connecting to VPN, please wait for connection", file=sys.stdout)

# connecting to VPN
os.system(r'"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" --command connect split_tunnel.ovpn')
time.sleep(3)

ip_address = "192.168.0.1"  # Replace this with the IP address you want to ping
max_attempts = 30  # Number of ping attempts before giving up
timeout_seconds = 5  # Time to wait between ping attempts (in seconds)

attempts = 0
while attempts < max_attempts:
    try:
        result = subprocess.run(["ping", ip_address, "-n", "1"], capture_output=True, text=True, check=True)
        print("Connected to VPN!")
        break
    except subprocess.CalledProcessError:
        print(f"Unable to ping IP {ip_address}.")

    # Wait for a moment before the next attempt
    print(f"Sleeping {timeout_seconds}")
    time.sleep(timeout_seconds)
    attempts += 1
    print(f"Attempt # {attempts}")

if attempts >= max_attempts:
    print(f"Could not ping IP {ip_address} after {max_attempts} attempts.")
    input()
    exit()

# Mounting Drive  Make sure root folder only contains files and no directories
print("Mounting Drive", file=sys.stdout)
os.system(r"net use W: {mount\folder} {password} /user:{user} /persistent:no")
time.sleep(3)

# requested files
print("The requested files are as follows: ", file=sys.stdout)
for dirs, folders, files in os.walk("W:\\"):
    for file in files:
        print(file, file=sys.stdout)

# check Location for available space windows
total_l, used_l, free_l = disk_usage(os.path.realpath('C:\\'))
free_mb = (free_l / 1000000)

# wanted file size server
size = 0
for ele in os.scandir('W:\\'):
    size += os.path.getsize(ele)
total_server = (size / 1000000)

print("You have: ", free_mb, " MB and Requested: ", total_server, " MB")

# chck to see if space is good
if free_mb > total_server:
    print("You have enough space!", file=sys.stdout)
else:
    print("not enough space, delete media before retrying!", file=sys.stdout)
    os.system(r"net use W: /Delete")
    os.system(r'"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" --command disconnect split_tunnel.ovpn')
    input()  # used to keep cmd window open
    exit()

os.makedirs("path\\for\\media\\save", exist_ok=True)

time.sleep(8)
# copying files   Ensure paths are correct
os.system(r'"py C:\scripts\copy_status.py W:\ path\\for\\media\\save"') #may be python.exe instead of py

# unmounting Drive
print("Unmounting drive", file=sys.stdout)
os.system(r"net use W: /Delete")

os.system(r'"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" --command disconnect split_tunnel.ovpn')
print("Disconnected from VPN", file=sys.stdout)

print("Enjoy your Media!", file=sys.stdout)
input()  # used to keep cmd window open
