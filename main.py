#!/usr/bin/env python
import os, time, socket, signal, sys, subprocess, shutil
from modules import *

netcheck()


clear()


def start(browser):
    os.system("sudo service tor start")
    os.system("proxychains "+browser)


def check(browsername,brow):
    chx = os.path.isfile("/bin/"+brow)
    if chx == True:
        pass
    elif chx == False:
        print(Kirmizi+browsername+" Not Found")
        exit()

banner = Mavi+"""

.▄▄ · ▄▄▄▄▄▄▄▄   ▄▄▄·  ▐ ▄  ▄▄ • ▄▄▄ .▄▄▄  
▐█ ▀. •██  ▀▄ █·▐█ ▀█ •█▌▐█▐█ ▀ ▪▀▄.▀·▀▄ █·
▄▀▀▀█▄ ▐█.▪▐▀▀▄ ▄█▀▀█ ▐█▐▐▌▄█ ▀█▄▐▀▀▪▄▐▀▀▄ 
▐█▄▪▐█ ▐█▌·▐█•█▌▐█ ▪▐▌██▐█▌▐█▄▪▐█▐█▄▄▌▐█•█▌
 ▀▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ ▀▀ █▪·▀▀▀▀  ▀▀▀ .▀  ▀

        [1]Firefox              [2]Google

"""
print(banner)
selection = input(Beyaz+"Which browser should we use? ===>")


if selection == "1":
    check("Firefox","firefox")
    start("firefox")

elif selection == "2":
    check("Chrome","google-chrome")
    start("google-chrome")


def keyboardinterrupt(sig, frame):
    print(Yesil+'Thanks for using my tool')
    os.system("service tor stop")
    os.system("exit")

signal.signal(signal.SIGINT, keyboardinterrupt)
signal.pause()
