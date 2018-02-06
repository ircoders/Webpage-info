#!/usr/lib/python2.7
# -*- coding: utf-8 -*-

import os
import random
from socket import *
import sys
import time

try:
    from colorama import *
    r = Fore.RED
    g = Fore.GREEN
    w = Fore.WHITE
    b = Fore.BLUE
    y = Fore.YELLOW
    m = Fore.MAGENTA
    res = Style.RESET_ALL
except ImportError:
    print '[*] First Import Colorama Module !'
    print '[*] Command --> sudo pip install colorama'
    sys.exit()
    
try:
    import requests
except ImportError:
    print '[*] First Import requests Module !'
    print '[*] Command --> sudo pip install requests'

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])
    
def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = '''
    
 /$$$$$$ /$$$$$$$   /$$$$$$ iraniancoders.ir /$$                              
|_  $$_/| $$__  $$ /$$__  $$                | $$                              
  | $$  | $$  \ $$| $$  \__/  /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$$
  | $$  | $$$$$$$/| $$       /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$_____/
  | $$  | $$__  $$| $$      | $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/|  $$$$$$ 
  | $$  | $$  \ $$| $$    $$| $$  | $$| $$  | $$| $$_____/| $$       \____  $$
 /$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$       /$$$$$$$/
|______/|__/  |__/ \______/  \______/  \_______/ \_______/|__/      |_______/ 
                  IRC Webpage Info V1.0                                                                                                                                                                                                       
    '''
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.07)
cls()
print_logo()

def GoodBye():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    
    g = '''
  /$$$$$$       iraniancoders.ir     /$$ /$$$$$$$                     
 /$$__  $$                          | $$| $$__  $$                    
| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$| $$  \ $$ /$$   /$$  /$$$$$$ 
| $$ /$$$$ /$$__  $$ /$$__  $$ /$$__  $$| $$$$$$$ | $$  | $$ /$$__  $$
| $$|_  $$| $$  \ $$| $$  \ $$| $$  | $$| $$__  $$| $$  | $$| $$$$$$$$
| $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$  \ $$| $$  | $$| $$_____/
|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$$|  $$$$$$$
 \______/  \______/  \______/  \_______/|_______/  \____  $$ \_______/
                                                   /$$  | $$          
                                                  |  $$$$$$/          
              IRC Webpage Info V1.0                \______/           
    '''
    for N, line in enumerate(g.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
        
def main():
    while True:
        print r + '---------------------------------------------------'
        geturl = raw_input(r + 'Enter URL : ')

        openurl = requests.get('http://' + geturl, timeout=5)

        cls()
        print_logo()
        print '\t\t' + r + 'URL ' + g + '--> ' + y + geturl
        print r + '---------------------------------------------------'
        print r + '[' + y + '1' + r + '] ' + g + 'Get Ip Address'
        print r + '[' + y + '2' + r + '] ' + g + 'Get Cookies'
        print r + '[' + y + '3' + r + '] ' + g + 'Get Status Code'
        print r + '[' + y + '4' + r + '] ' + g + 'Get Headers'
        print r + '[' + y + '5' + r + '] ' + g + 'View ' + r + geturl + g + ' Source'
        print r + '[' + y + '6' + r + '] ' + g + 'Download ' + r + geturl + g + ' Source'
        print r + '[' + y + '99' + r + '] ' + g + 'Exit'
        print r + '---------------------------------------------------\n'


        getmethod = raw_input(m + 'Enter Your Method : ')

        if getmethod == '1':
            getip = gethostbyname(geturl)
            cls()
            print_logo()
            print r + '---------------------------------------------------'
            print r + 'IP ' + g + '--> ' + y + str(getip)

        elif getmethod == '2':
            getcookies = openurl.cookies
            cls()
            print_logo()
            print r + '---------------------------------------------------'
            print r + 'Cookies ' + g + '--> ' + y + str(getcookies)

        elif getmethod == '3':
            getstatus = openurl.status_code
            cls()
            print_logo()
            print r + '---------------------------------------------------'
            print r + 'Status Code ' + g + '--> ' + y + str(getstatus)

        elif getmethod == '4':
            getheader = openurl.headers
            cls()
            print_logo()
            print r + '---------------------------------------------------'
            print r + 'Headers ' + g + '--> ' + str(getheader)

        elif getmethod == '5':
            viewsource = openurl.content
            cls()
            print_logo()
            print r + '---------------------------------------------------'
            print r + 'Source ' + g + '-->' 
            time.sleep(0.05)
            print viewsource
        elif getmethod == '6':
            file = open('result.html', 'w')
            file.write(openurl.content)
            file.close()
            cls()
            print_logo()
            print r + '---------------------------------------------------'
            print r + 'Source Saved to ' + g + '--> ' + y + 'result.html'

        elif getmethod == '99':
            cls()
            GoodBye()
            break

        else:
            cls()
            print_logo()
            print r + '---------------------------------------------------'
            print r + 'Unknown Input'

        
         

if __name__ == '__main__': main()
