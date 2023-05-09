from instagramapi import *
import time
import sys

init("C:\\Program Files (x86)\\chromedriver.exe")

#---#   START login seqeunce 
Uname = str(input("Username: "))
Upass = str(input("Password: "))

login(Uname, Upass)
#---#   END login sequence

goHome()
debug()

if str(input("Quit (y/n): ")).upper() == "Y":
    quit()
    sys.exit()