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
        if driver.current_url() == "https://www.instagram.com/accounts/onetap/?next=%2F":
            print("save login?")

def quit():
    '''
    - quit selenium
    '''
    global driver
    driver.quit()

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
    try:
        global driver 
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div/a/div').click()
        time.sleep(1)
        return True 
    except:
        return False 
    finally:
        if driver.current_url() == "https://www.instagram.com/?next=%2F":
            print("enable notifications?")
    
def goSearch():
    try:
        return True 
    except:
        return False 

def goExplore():
    try:
        return True 
    except:
        return False 

def goReels():
    try:
        return True 
    except:
        return False  

def goMessages():
    try:
        return True 
    except:
        return False 

def goNotifications():
    try:
        return True 
    except:
        return False  

def goCreate():
    try:
        return True 
    except:
        return False  

def goProfile():
    try:
        return True 
    except:
        return False         