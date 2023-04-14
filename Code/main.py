import sys


def main():
    from Frontend import printLogo
    from Backend import esc_key_pressed
    from instagrapi import Client
    from getpass import getpass
    
    import argparse        
    import time       
    import os
    import re
    
    #---# init program: clear screen, display logo

    os.system("cls")
    printLogo("green")

    #---# init user: grab login and login to account

    cl = Client()

    while True:
        if esc_key_pressed == True:
            print("Quiting program...")
            return
        try:
            username = str(input("USERNAME: "))
            password = getpass("PASSWORD: ")
            cl.login(username, password)
            print(f"\nLogin Successful")
            time.sleep(1)
            os.system("cls")
            printLogo("green")
            break 
        except:
            os.system("cls")
            printLogo("green")
            print(f"\nERROR: could not login\n")
            pass

    #---# get target user info

    while True:  
    
        client_following = cl.user_following(cl.user_id_from_username(username))

        while True:
            try:
                target_username = str(input(f"\nTARGET USERNAME: "))
                target_user_id   = cl.user_id_from_username(target_username)
                break 
            except:
                print("Could not find user...")
        target_user_info = cl.user_info(target_user_id)
        target_user_bio  = target_user_info.biography.replace("                                                    ","\n\t\t\t ")

        print(f"\nUSER INFO:\n")
        print("\tUSER ID:\t", target_user_id)
        print("\tVERIFIED:\t", target_user_info.is_verified)
        print("\tBIO:\t\t", target_user_bio)
        print("\tMEDIA COUNT:\t", target_user_info.media_count)
        print("\tFOLLOWERS:\t", target_user_info.follower_count)
        print("\tFOLLOWING:\t", target_user_info.following_count)
        print("\tPROFILE PIC:\t", target_user_info.profile_pic_url)

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
    sys.exit()
