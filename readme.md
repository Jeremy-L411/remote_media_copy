# Remote Media Copy automation

### I created this program to help transfer files from computers from my NAS to where I did not have to remote in and verify that the files were transftered. 
### I wanted a simple solution where all you had to do was double click an icon and it executed. 
### This script I have tested on windows 10-11, using Python 3.11 and OpenVPN 2.5.8. I am sure it will work with other versions. 
### copy_status.py needs to remain separate and I typically just put it in C:\scripts so it is out of the way. 
### Executing the python script has changed depending on how I loaded Python on the computer. Sometimes I needed python.exe, others just py worked. 
### I want to figure out how to have a check to see if the VPN is established in a loop to negate the counting and speed things up if the connection is quick. 
### I had modified rich.progress in order to suite this project. Rich initially only worked for a single file, modified it to work with a batch of single files, no folders will work in this script. 
### The NAS I tested this on is Linux based, in order to test an array of files I also used `touch newfile{1..10}` to test multiple files. I also wanted to test if the size worked and utalized `truncate -s 40G file.img` to simulate a very large file. I tested upwards of 100 files and executed well. When avaliable space is less than requested space it gets caught and stops. 
