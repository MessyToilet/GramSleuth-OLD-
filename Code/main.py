

def main():
    from Frontend import printLogo
    from instagrapi import Client
    from getpass import getpass
    import argparse        
    import time       
    import sys
    
    #---# init program: display logo

    printLogo("green")

    #---# init user: grab login and login to account

    cl = Client()

    while True:
        try:
            username = str(input("EMAIL: "))
            password = getpass("PASSWORD: ")

            cl.login(username, password)
            print(f"Login Successful")
            break 
        except:
            print(f"\nERROR: could not login\n")
            pass


    return

if __name__ == '__main__':
    main()
