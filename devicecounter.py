import os
import re

#Just for aesthetic
os.system("clear")

#Sample format

#Nmap scan report for 10.32.228.1
#Host is up (0.010s latency).
#MAC Address: 20:A6:80:14:0F:26 (Huawei Technologies)

print("Scanning for devices, should take 5-60s.")

##MAKE SURE TO UPDATE THE IP ADDRESS IF YOU WANT TO RUN THIS ON A DIFFERENT WIFI NETWORK
#REPLACE ONLY THE &s     &&&.&&&.&                    
os.system("sudo nmap -sn 192.168.0.0/24 > devices.log 2>> err.log")


device_list = []

#format: <device manufacturer> : <count>
manu_count = {}

print("Scan completed successfully.\nOpening file devices.log...")
with open("devices.log") as d:
    init_time = ""
    for line in d.readlines():
        if "Starting Nmap" in line:
            init_time = line[45:]
            print("Scan started at: {}".format(init_time))
        elif "Nmap scan report for " in line:            
            rec = False
            ipaddr = ""

            for character in line:
                try:
                    int(character)
                    ipaddr += character
                    rec = True
                except ValueError:
                    if character == "." and rec == True:
                        ipaddr += character
            
        elif "MAC Address: " in line:
            macaddr = ""
            mac_rec = False
            colon_spotted = False
            
            manu = ""
            manu_rec = False
            parenth_count = 0
            
            for character in line:
                if character == ":":
                    if mac_rec == False:
                        colon_spotted = True
                    elif mac_rec == True:
                        colon_spotted = False
                        macaddr += character

                elif character == " ":
                    if colon_spotted == True:
                        mac_rec = True
                    else:
                        mac_rec = False
                elif mac_rec == True:
                    macaddr += character
                

                if character == "(":
                    parenth_count += 1
                    manu_rec = True
                elif character == ")":
                    if parenth_count == 1:
                        manu_rec = False
                    elif parenth_count > 1:
                        parenth_count -= 1
                elif manu_rec == True:
                    manu += character


            device_list.append([ipaddr, manu, macaddr])
        
        elif "Nmap done:" in line:
            hostcount = ""
            rec = False
            for character in line:
                if character == "(":
                    rec = True
                elif rec == True:
                    hostcount = character
                    rec = False
            hostcount = str(int(hostcount) - 1)
            print("{} devices found".format(hostcount))


for device in device_list:
    print("\nIP Address: {}\nManufacturer: {}\nMAC Address: {}".format(device[0], device[1], device[2]))                    

