import requests
import os
import sys
import time

print ("\033[31m")


os.system("figlet Hallo To Moaz Mohamed Script ")

time.sleep(3)

os.system("clear")

print ("\033[1;31m")

os.system("figlet INFO IP ")


print ("\033[1;35m By:MoazMohamed")



print ("\033[1;32m")
ip = input("Enter IP Address:\033[1;31m ").strip()

url = "http://ip-api.com/json/{0}"
response = requests.get(url.format(ip)).json()

for key in response:
    print ("\033[34m{0: <15} \033[1;35m- \033[1;36m{1}".format(key, response[key]))
