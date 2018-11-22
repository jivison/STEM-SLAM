import os

def run(target_ip):

    ##MAKE SURE TO UPDATE THE IP ADDRESS IF YOU WANT TO RUN THIS ON A DIFFERENT WIFI NETWORK
    #REPLACE ONLY THE &s     &&&.&&&.&                    
    os.system("sudo nmap -sn {}.0/24 > devices/devices.log".format(target_ip))

    #Interpreting the output from the nmap command
    with open("devices/devices.log", "r") as d:

        hostcount = ""

        for line in d.readlines():
            
            #Looking for the number of devices   
            if "Nmap done:" in line:
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
        os.system("cp devices/devices.log devices/devices.log.backup; > devices/devices.log")

    
    return hostcount