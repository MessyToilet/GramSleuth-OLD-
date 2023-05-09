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
time.sleep(5)
goSearch()
time.sleep(5)
goExplore()
time.sleep(5)
goReels()
time.sleep(5)
goMessages()
time.sleep(5)
goNotifications()
time.sleep(5)
goProfile()

if str(input("Quit (y/n): ")).upper() == "Y":
    quit()
    sys.exit()