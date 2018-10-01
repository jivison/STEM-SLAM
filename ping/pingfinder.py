import os

#Sample ping output

#PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
#
#--- 8.8.8.8 ping statistics ---
#10 packets transmitted, 9 received, 10% packet loss, time 9041ms
#rtt min/avg/max/mdev = 7.182/14.191/31.548/8.386 ms

print("Pinging Google (8.8.8.8)")
os.system("ping -c 10 -q 8.8.8.8 > ping.log")

with open("ping.log") as p:
        
        rec = False
        avg_ping_time = ""

        for line in p.readlines():
            if "rtt min/" in line:
                
                numbers = False
                
                for char in line:
                    if char == "=":
                        numbers = True            
                    
                    elif char == "/":
                        if numbers == True:
                            rec = True
                            numbers = False
                        elif rec == True:
                            break

                    try:
                        if rec == True:
                            avg_ping_time += str(int(char))
                    except ValueError:
                        if char == "." and rec == True:
                            avg_ping_time += "."
                        
            


os.system("cp ping.log ping.log.backup; > ping.log")

print("Average ping time over 10 packets: {}".format(avg_ping_time))

#Appends all of the nmap data to the csv file
with open("../networkdetails.csv", "a+") as csv:
    csv.write(",{}ms".format(avg_ping_time))
