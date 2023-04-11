

def main():
    
    from Frontend import printLogo
    from instagrapi import Client
    from getpass import getpass
    import argparse        
    import time       
    import sys
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
            time.sleep(2)
            os.system("cls")
            printLogo("green")
            break 
        except:
            os.system("cls")
            printLogo("green")
            print(f"\nERROR: could not login\n")
            pass

    #---# get target user

    while True:
        os.system("cls")
        printLogo("green")

        target_user_id = cl.user_id_from_username(str(input(f"TARGET USERNAME: ")))
 
        print(f"\nUSER INFO:\n")
        print("\tUSER ID:", target_user_id)
        print("\tFOLLOWING:", len(cl.user_following(target_user_id, 10)))
        print("\tFOLLOWING:", len(cl.user_following_gql(target_user_id, 10)))
        print("\tFOLLOWERS:", len(cl.user_followers(target_user_id, 10)))
        print("\tFOLLOWERS:", len(cl.user_followers_gql(target_user_id, 10)))

    return

if __name__ == '__main__':
    main()
