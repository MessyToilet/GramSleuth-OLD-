from Backend import *
from Frontend import *

def main():
    from instagrapi import Client
    from getpass import getpass
    
    import argparse        
    import time       
    import re

    #---# init user: grab login and login to account

    cl = Client()

    loginPassed = False
    while not loginPassed:
        printLogo("green")
        username = str(input("USERNAME: "))
        password = getpass("PASSWORD: ")

        if username == "!" or password == "!":
            endProgram()
            continue

        loginPassed = login(username, password)


    #---# get target user info

    while True:  
        while True:
            target_username = str(input(f"\nTARGET USERNAME: "))
 
            if target_username == "!":
                endProgram()
                continue
            
            if isinstance(targetUserID(target_username), dict):
                print(f"user found")
                break


            

        print(f"\nUSER INFO:\n")
        print("\tUSER ID:\t", targetUserID(target_username))
        print("\tVERIFIED:\t", targetUserID(target_username).is_verified)
        print("\tBIO:\t\t", targetUserID(target_username))
        print("\tMEDIA COUNT:\t", targetUserID(target_username).media_count)
        print("\tFOLLOWERS:\t", targetUserID(target_username).follower_count)
        print("\tFOLLOWING:\t", targetUserID(target_username).following_count)
        print("\tPROFILE PIC:\t", targetUserID(target_username).profile_pic_url)

        if str(input(f"\nIS THIS CORRECT USER? (y/n): ")).upper() not in ["N", "NO"]:
        
            print("\n\tPRIVATE:\t",target_user_info.is_private)
            if target_user_info.is_private == True and target_user_info.username not in client_following:
                
                print("\t\t\t you will need to sign into an account following the target or request to follow...")
                if str(input(f"\nREQUEST TO FOLLOW? (y/n): ")).upper() in ["Y", "YES"]:
                    cl.user_follow(target_user_id)
                    print("Requested to follow...")

        


        

        

    return

if __name__ == '__main__':
    main()

