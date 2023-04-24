#---# Imports

from instagrapi import Client 
from getpass import getpass

#---# Init

cl = Client()

#---# Functions

def login(username, password):
    try:
        cl.login(username, password)
        print(f"\nLogin Successful")
        return True 
    except:
        print("\nERROR: could not login")
        return False

def userInfo(targetUser):
    return True

def getBotsFollowing():
    return True

def getBotFollowers():
    return True

def getGhostsFollowing():
    return True

def getGhostFollowers():
    return True

