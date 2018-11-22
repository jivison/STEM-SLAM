import os

def run():

    os.system("ping -c 10 -q 8.8.8.8 > ping/ping.log")

    with open("ping/ping.log") as p:
            
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
                            

    os.system("cp ping/ping.log ping/ping.log.backup; > ping/ping.log")

    return avg_ping_time