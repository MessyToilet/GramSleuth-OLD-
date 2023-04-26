#---# Imports

from instagrapi import Client 
from getpass import getpass

#---# Init

cl = Client()

#---# Functions

def login(username, password):
    global userName                                                                         #bring in global var
    proxyList = [["PROXY NAME", "PROXY ADDRESS"]]                                           #list of free proxies
    try:
        cl.login(username, password)                                                        #try login
        userName = username
        print(f"\nLogin Successful")                                                        #print login successful
        try:
            if str(input("Do you have your own proxy? (y/n): ")).upper() == "Y":            #if user had paid proxy
                try:
                    print(f"Setting proxy...")
                    cl.set_proxy(str(input("Proxy Address: ")))                             #try to join paid proxy
                    print(f"Proxy Set :)")                                                  #print success
                    return True                                                             #end func
                except:
                    print(f"ERROR: Proxy login failed, trying free proxy sites...")         #if ERROR in proxy print error
            print(f"Setting proxy...")                              
            cl.set_proxy("socks5://127.0.0.1:30235")                                        #Try joining free proxy
            print(f"Proxy set :)")
        except:
            print(f'ERROR: could not set proxy')                                            #if ERROR joining free proxy print error
            return False
        return True 
    except:
        print("\nERROR: could not login")                                                   #if ERROR loging in print error
        return False

def targetUserID(targetUser):
    if targetUser in targetUserID:
        return targetUserID.get(targetUser)
    else:
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

