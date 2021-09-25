import sys
import os
import time

green = "\033[32;1m" # Green light

ip = raw_input("IP address : ")

os.system("clear")
os.system("figlet PING!")
print ("LOADING!!!!")
time.sleep(2)
os.system("clear")
print ("starting!")
os.system('ping ' + ip)
