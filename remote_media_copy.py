import os
import time
import sys
from shutil import disk_usage


# todo check to see if VPN is connected to pass the connection, put in loop until connection established

print("connecting to VPN, waiting 90 seconds for secure connection", file=sys.stdout)

# connecting to VPN
os.system(r'"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" --command connect split_tunnel.ovpn')
time.sleep(3)

# Sometimes it takes a while for VPN to connect, this just waits until the loop can be made
for i in range(90):
    print(i, file=sys.stdout)
    time.sleep(1)

# Mounting Drive  Make sure root folder only contains files and no directories
print("Mounting Drive", file=sys.stdout)
os.system(r"net use W: *remote_path* *password* /user:usr /persistent:no")

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


time.sleep(8)
# copying files   Ensure paths are correct
os.system(r"python.exe C:\scripts\copy_status.py W:\*folder* C:\Users\User\Desktop") #may be py instead of python.exe

# unmounting Drive
print("Unmounting drive", file=sys.stdout)
os.system(r"net use W: /Delete")

os.system(r'"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" --command disconnect split_tunnel.ovpn')
print("Disconnected from VPN", file=sys.stdout)

print("Enjoy your Media!", file=sys.stdout)
input()  # used to keep cmd window open
