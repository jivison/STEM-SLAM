import os

#Sample format

#Nmap scan report for 10.32.228.1
#Host is up (0.010s latency).
#MAC Address: 20:A6:80:14:0F:26 (Huawei Technologies)

print("Scanning for devices, should take 5-60s.")

os.system("echo \"If prompted for a password, it is only used to run the nmap command.\"")

##MAKE SURE TO UPDATE THE IP ADDRESS IF YOU WANT TO RUN THIS ON A DIFFERENT WIFI NETWORK
#REPLACE ONLY THE &s     &&&.&&&.&                    
os.system("sudo nmap -sn 10.32.228.0/24 > devices.log")

#format: [<ip address>, <manufacturer>, <mac address>]
device_list = []

#format: <device manufacturer> : <count>
manu_count = {}

#The time when the scan started
init_time = ""

print("Scan completed successfully.\nOpening file devices.log...")

#Interpreting the output from the nmap command
with open("devices.log", "r") as d:
    for line in d.readlines():
        
        #Recording the time of the scan (non-dynamic)
        if "Starting Nmap" in line:
            init_time = line[45:]
            print("Scan started at: {}".format(init_time))
        
        #Looking for the ip address
        elif "Nmap scan report for " in line:            
            rec = False
            ipaddr = ""

            #Garbage spaghetti code looking for everything between the dots (theoretically dynamic)

            for character in line:
                try:
                    int(character)
                    ipaddr += character
                    rec = True
                except ValueError:
                    if character == "." and rec == True:
                        ipaddr += character
            
        #Looking for MAC address and manufacturer
        elif "MAC Address: " in line:
            macaddr = ""
            mac_rec = False
            colon_spotted = False
            
            manu = ""
            manu_rec = False
            parenth_count = 0

            for character in line:
                
                #More garbage spaghetti code looking for stuff after a first colon (non-dynamic)

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
                
                #Even more garbage spaghetti code looking for stuff between brackets

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

            #Adds all of the information the program just found to device_list
            device_list.append([ipaddr, manu, macaddr])

            #Counting the nummber of each manufacturer
            try:
                manu_count[manu] += 1
            except Exception:
                manu_count[manu] = 1

        #Looking for the number of devices   
        elif "Nmap done:" in line:
            hostcount = ""
            rec = False
            for character in line:
                if character == "(":
                    rec = True
                elif rec == True:
                    hostcount = character
                    rec = False
           
            #Substracts 1 because nmap always counts an extra device
            hostcount = str(int(hostcount) - 1)

    #Wipes devices.log but also creates a backup
    os.system("cp devices.log devices.log.backup; > devices.log")

#The manu count has commas, which is incompatable with a csv file
def fix_manu_count():
    output = "{"
    for manufacturer in manu_count:
        output += "{}:{}|".format(manufacturer, manu_count[manufacturer])
    output = output[:-1] + "}"
    return output

#Appends all of the nmap data to the csv file
with open("../networkdetails.csv", "a+") as csv:
    csv.write("\n{},{},{}".format(init_time[:-1], str(int(len(device_list))-1), fix_manu_count()))
    