import os, time, subprocess
from modules import *

checkroot("""
    Please Put Sudo Before Command!!!

    Example Usage: sudo main.py
    """,Kirmizi)

netcheck()
clear()
sayac = 0

while True:
    conffile = open("/etc/proxychains.conf","w")

    dosya = open("./proxychains.conf","r")
    conffile.writelines(dosya.readlines())
    sayac+=1
    if sayac == 5783:
        exit()