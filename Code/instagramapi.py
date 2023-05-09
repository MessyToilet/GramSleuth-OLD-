from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time


#---#   Start up funcs


def init(PATH):
    '''
    - take path from user
    - globalize driver
    - init with chrome webdriver
    - connect to instagram 
    - retrun true is passed, false otherwise
    '''
    try:
        global driver
        driver = webdriver.Chrome(PATH)
        driver.get("https://www.instagram.com/")
        return True
    except:
        return False
    
def login(username, password):
    '''
    - take username and password from user
    - globalize driver
    - find username element by name and input the username
    - find password element by name and input the password
    - find login button from xpath and click
    - return true if passed false otherwise
    - sleep is used to avoid detection
    - if login failed due to bad creds tell user and quit program
    - if bot runs into save login option prompt user
    '''
    try:
        global driver
        driver.find_element(By.NAME, "username").send_keys(str(username))            
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys(str(password))
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(5)
        return True
    except:
        return False
    finally:
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[2]/p')       
            print('ERROR: "There was a problem logging you into Instagram. Please try again soon."')
            print("Quiting...")
            driver.quit()
            return False
        except:
            pass
        if driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F":
            if str(input("Save login? (y/n): ")).upper() == "Y":
                if str(input("It is not recomended to save login, do you wish to continue (y/n): ")).upper() == "Y":
                    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button').click()
            else:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()

def quit():
    '''
    - quit selenium
    '''
    global driver
    driver.quit()
    return
    
def debug():
    from bs4 import BeautifulSoup
    global driver

    soup = BeautifulSoup(driver.page_source) 

    for tag in soup.find_all('title'):
        print(tag.text)

    print(driver.page_source)
    print(driver.current_url)


#---#   Low Level Actions


def goHome():
    '''
    - globalize driver
    - find home button by xpath and click
    - return true if passed, return false otherwise
    - if bot runs into enable notifs option prompt user
    - sleep is used to avoid detection
    '''
    try:
        global driver 
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div/a/div').click()
        time.sleep(1)
        return True 
    except:
        return False 
    finally:
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]')
            if str(input("Enable notifications? (y/n): ")).upper() == "Y":
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]').click()
            else:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        except:
            pass

def goSearch(user=True):
    """
    - globalize driver
    - find search by xpath and click
    - return true if passed, false otherwise
    - sleep is used to avoid detection
    """
    if user == True:
        try:
            global driver
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a').click()
            time.sleep(1)
            return True 
        except:
            return False 
    else:
        pass #send keys

def goExplore():
    """
    - globalize driver
    - find element by xpath and click 
    - return true if passed, flase otherwise
    - sleep is used to avoid detection
    """
    try:
        global driver
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[3]/div/a').click()
        time.sleep(1)
        return True 
    except:
        return False 

def goReels():
    """
    - globalize driver
    - find element by xpath and click
    - return true if passed, false otherwise 
    - sleep is used to avoid detection
    """
    try:
        global driver 
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[4]/div/a').click()
        time.sleep(1)
        return True 
    except:
        return False  

def goMessages():
    """
    - globalize driver
    - find element by xpath and click
    - return true if passed, flase otherwise
    - sleep is used to avoid detection
    """
    try:
        global driver
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/a').click()
        time.sleep(1)
        return True 
    except:
        return False 

def goNotifications():
    """
    - globlalize driver
    - find element by xpath and click
    - return true if passed, false otherwise
    - sleep is used to avoid detection
    """
    try:
        global driver 
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[6]/div/a').click()
        time.sleep(1)
        return True 
    except:
        return False  

def goCreate():
    """
    - globlalize driver
    - find element by xpath and click
    - return true if passed, false otherwise
    - sleep is used to avoid detection
    """
    try:
        global driver 
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a').click()
        time.sleep(1)
        return True 
    except:
        return False  

def goProfile():
    """
    - globlalize driver
    - find element by xpath and click
    - return true if passed, false otherwise
    - sleep is used to avoid detection
    """
    try:
        global driver
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/div/a").click()
        time.sleep(1)
        return True 
    except:
        return False         

def goMore():
    """
    - globlalize driver
    - find element by xpath and click
    - return true if passed, false otherwise
    - sleep is used to avoid detection
    """
    try:
        global driver
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div/a').click()
        time.sleep(1)
        return True 
    except:
        return False


#---#   Mid Level Actions


def getInfo(user=True):
    global driver
    if user == True:
        goProfile()
        getFollowers()
        getFollowing()
    else:
        goSearch(user)
        

def getFollowers(user=True):
    global driver
    if user == True:
        goProfile()
    else:
        goSearch(user)

def getFollowing(user=True):
    global driver
    if user == True:
        goProfile()
    else:
        goSearch(user)


#---# High Level Actions 


def findGhostFollowers(user=True):
    return 

def findBotFollowers(user=True):
    return 

def findGhostFollowing(user=True):
    return 

def findBotFollowing(user=True):
    return 

def parseBio(bio_element):
    return
