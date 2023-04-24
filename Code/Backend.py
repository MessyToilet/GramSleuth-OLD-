#---# Imports

from instagrapi import Client 
from getpass import getpass

#---# Init

cl = Client()

#---# Functions

def login(username, password):
    global userName
    try:
        cl.login(username, password)
        userName = username
        print(f"\nLogin Successful")
        return True 
    except:
        print("\nERROR: could not login")
        return False

def targetUserID(targetUser):
    try:
        return targetUserID.get(targetUser)
    except:
        try:
            TarUsID = cl.user_id_from_username(targetUser)
            targetUserID.add(targetUser, TarUsID)
            return targetUserID.get(targetUser)
        except:
            print("\nERROR: couldn't find user")
            return False
    

def userInfo(targetUser):
    return True

def getBotsFollowing(targetUser):
    return True

def getBotFollowers(targetUser):
    return True

def getGhostsFollowing(targetUser):
    return True

def getGhostFollowers(targetUser):
    return True

def endProgram():
    import sys
    import os
    
    if str(input("confirm quit program (y/n): ")).upper() == "Y":
        print("QUITING PROGRAM...")
        os.system("cls")
        sys.exit()
    else:
        return
    
#---# Global Vars
userName = ""
targetUserID = {}

userFollowing = []
targetUserFollowing = {}

userFollowers = []
targetUserFollowers = {}

userBio = ""
targetUserBio = {}

