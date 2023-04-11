import sys

def main():
    from Frontend import printLogo
    from instagrapi import Client
    from getpass import getpass
    import argparse        
    import time       
    import os
    
    #---# init program: clear screen, display logo

    os.system("cls")
    printLogo("green")

    #---# init user: grab login and login to account

    cl = Client()

    while True:
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
        target_user_id   = cl.user_id_from_username(str(input(f"TARGET USERNAME: ")))
        target_user_info = cl.user_info(target_user_id)
        target_user_bio  = target_user_info.biography.replace("                                                    ","\n\t\t\t ")

        print(f"\nUSER INFO:\n")
        print("\tUSER ID:\t", target_user_id)
        print("\tBIO:\t\t", target_user_bio)
        print("\tFOLLOWERS:\t", target_user_info.follower_count)
        print("\tFOLLOWING:\t", target_user_info.following_count)
        print("\tPROFILE PIC:\t", target_user_info.profile_pic_url)

        if str(input(f"\nIS THIS CORRECT USER? (y/n): ")).upper() in ["N", "NO"]:
            pass 

        


        

    return

if __name__ == '__main__':
    main()
    sys.exit()
