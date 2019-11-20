import requests
import re
import os
import sys
import time



lines = []



print(lines)
with open("portim.txt", 'r') as file:
    lines = file.readlines()

def logo():
    l = '''\033[1m\033[94m
    ----------------------------------------------------------
     _______  _______  ______    _______  _______  ______   
    |       ||       ||    _ |  |       ||       ||    _ |  
    |    _  ||   _   ||   | ||  |_     _||    ___||   | ||  
    |   |_| ||  | |  ||   |_||_   |   |  |   |___ |   |_||_ 
    |    ___||  |_|  ||    __  |  |   |  |    ___||    __  |
    |   |    |       ||   |  | |  |   |  |   |___ |   |  | |
    |___|    |_______||___|  |_|  |___|  |_______||___|  |_|
    
                Coded By SaharAvitan(AttacKit)            
                    attackit.hack@gmail.com
    ----------------------------------------------------------
    '''
    print(l)


def clear():
    os_name = os.name
    if os_name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def progress():
    for i in range(1, 20):
        print("\r\033[1m\033[91m" + "/-\|"[i % 4] + str(int((i / 20.0) * 100)) + "%" + "[" + ("#" * i).ljust(20, " ") + "]",time.sleep(0.1), end="")
        sys.stdout.flush()


clear()
logo()
progress()
clear()
logo()


port = input("\033[1m\033[92mWhich port would you like to look for?\nPort\033[0m: ")
print("")
while True:


    try:
        if int(port):
            c = 0
            for src in lines:
                try:
                    p = str(src)
                    r = re.search("<td>(.*)<td>(.*)<td>(.*)<td>(.*)", p)
                    port_scan = r.group(1)
                    protocol = r.group(2)
                    type = r.group(3)
                    vuln = r.group(4)
                    if vuln == "":
                        vuln = "Not found"

                    if port == port_scan:
                        c += 1
                        print("\033[1m\033[94mPort\033[0m: {}\n\033[1m\033[94mProtocol\033[0m: {}\n\033[1m\033[94"
                              "mType\033[0m: {}\n\033[1m\033[94mVulnerability\033[0m: {}\n-----------------------"
                              .format(port_scan, protocol, type, vuln))
                except:
                    pass
            if c == 0:
                print("\nNo vulnerabilities found for Port '{}'.\n".format(port))
            else:
                print("\nFound {} vulnerabilities\nThere is no more information for Port '{}'.\n".format(c, port))
    except:
        print("Invalid parameter\n")
    port = input("\033[1m\033[92mWhich port would you like to look for?\nPort\033[0m: ")
    print("")
    clear()
    logo()

