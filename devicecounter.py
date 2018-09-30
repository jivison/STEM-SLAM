import os

#Sample format

#Nmap scan report for 10.32.228.1
#Host is up (0.010s latency).
#MAC Address: 20:A6:80:14:0F:26 (Huawei Technologies)

print("Scanning for devices, should take 5-60s.")

os.system("echo \"If prompted for a password, it is only used to run the nmap command.\"")

##MAKE SURE TO UPDATE THE IP ADDRESS IF YOU WANT TO RUN THIS ON A DIFFERENT WIFI NETWORK
#REPLACE ONLY THE &s     &&&.&&&.&                    
os.system("sudo nmap -sn 192.168.1.0/24 > devices.log")

device_list = []

#format: <device manufacturer> : <count>
manu_count = {}

#The time when the scan started
init_time = ""

print("Scan completed successfully.\nOpening file devices.log...")
with open("devices.log", "r") as d:
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

            try:
                manu_count[manu] += 1
            except Exception:
                manu_count[manu] = 1

        
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

    os.system("cp devices.log devices.log.backup; > devices.log")

with open("devicehistory.csv", "a+") as csv:
    csv.write("\n{},{},{}".format(init_time[:-1], str(int(len(device_list))-1), (manu_count)))
    
