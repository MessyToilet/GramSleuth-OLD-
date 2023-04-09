
def pingInstagram(proxy_addr):
    import socket
    import socks

    socks.set_default_proxy(socks.SOCKS5, proxy_addr[0], proxy_addr[1])
    socket.socket = socks.socksocket
    
    try:
        # connect to Instagram
        with socket.create_connection(("https://www.instagram.com/", 80), timeout=10) as conn:
            pass
        print("Connected to Instagram")
        return True
    except OSError:
        pass
    print("Cannot connect to Instagram")
    return False




def startUpFail():
    import os
    from tqdm import tqdm
    import time

    CWD = os.getcwd()
    print(f"\ncurrent working directory: {CWD}")
    
    #check if needed files exist
    if not os.path.exists(os.path.join(CWD, "CLIside.py")) or not os.path.exists(os.path.join(CWD, "INSTAside.py")):
        print("ERROR: missing file(s)")
        return True
    else:
        print("ALL FILES EXIST :)")

    pingInstagram(("127.0.0.1", 30235))



def main():
    from CLIside import printLogo
    import argparse        
    import time       
    
    if startUpFail():
        return

    printLogo("green")

    return

if __name__ == '__main__':
    main()
