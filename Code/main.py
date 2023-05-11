from instagramapi import *
import time
import sys

init("GramSleuth\\requirments\\chromedriver.exe")

#---#   START login seqeunce 
Uname = str(input("Username: "))
Upass = str(input("Password: "))

login(Uname, Upass)
#---#   END login sequence

goProfile()

if str(input("Quit (y/n): ")).upper() == "Y":
    quit()
    sys.exit()