from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pickle as pk
import time

# ---#   Start up funcs

driver = webdriver.Chrome()


def init():
    """
    - take path from user
    - globalize driver
    - init with chrome webdriver
    - connect to instagram
    - add cookies
    - retrun true is passed, false otherwise
    """
    try:

        driver.get("https://www.instagram.com/")
        cookies = pk.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        return True
    except:
        return False


def login(username, password):
    """
    - take username and password from user
    - globalize driver
    - find username element by name and input the username
    - find password element by name and input the password
    - find login button from xpath and click
    - return true if passed false otherwise
    - sleep is used to avoid detection
    - if login failed due to bad creds tell user and quit program
    - if bot runs into save login option prompt user
    """
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
            driver.find_element(By.XPATH,
                                '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div['
                                '1]/div[2]/form/div[2]/p')
            print('ERROR: "There was a problem logging you into Instagram. Please try again soon."')
            print("Quiting...")
            driver.quit()
            return False
        except:
            pass
        if driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F":
            if str(input("Save login? (y/n): ")).upper() == "Y":
                if str(input("It is not recomended to save login, do you wish to continue (y/n): ")).upper() == "Y":
                    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div['
                                                  '2]/section/main/div/div/div/section/div/button').click()
            else:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div['
                                              '2]/section/main/div/div/div/div/div').click()


def quit():
    '''
    - save cookies
    - quit selenium
    '''

    pk.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    driver.quit()

    return


def debug():
    soup = BeautifulSoup(driver.page_source)

    for tag in soup.find_all('title'):
        print(tag.text)

    print(driver.page_source)
    print(driver.current_url)


# ---#   Low Level Actions


def goHome():
    """
    - globalize driver
    - find home button by xpath and click
    - return true if passed, return false otherwise
    - if bot runs into enable notifs option prompt user
    - sleep is used to avoid detection
    """
    try:
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div['
                            '2]/div[1]/div/div/a/div').click()
        time.sleep(1)
        return True
    except:
        return False
    finally:
        try:
            driver.find_element(By.XPATH,
                                '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]')
            if str(input("Enable notifications? (y/n): ")).upper() == "Y":
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div['
                                    '2]/div/div/div[3]/button[1]').click()
            else:
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div['
                                    '2]/div/div/div[3]/button[2]').click()
        except:
            pass


def goSearch(user=True):
    """
    - globalize driver
    - find search by xpath and click
    - return true if passed, false otherwise
    - goSearch is also used to reach a users profile
    - sleep is used to avoid detection
    """
    try:
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div['
                            '2]/div[2]/div/a').click()
        time.sleep(1)
        if not user:
            try:
                sendKeys(user)
                driver.send_keys(Keys.ARROW_DOWN)
                driver.send_Keys(Keys.RETURN)
                return True
            except:
                return False
        else:
            return True
    except:
        return False


def goExplore():
    """
    - globalize driver
    - find element by xpath and click 
    - return true if passed, flase otherwise
    - sleep is used to avoid detection
    """
    try:
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div['
                            '2]/div[3]/div/a').click()
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
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div['
                            '2]/div[4]/div/a').click()
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
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div['
                            '2]/div[5]/div/div/a').click()
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
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div['
                            '2]/div[6]/div/a').click()
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
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a').click()
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
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/div/a").click()
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
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div/a').click()
        time.sleep(1)
        return True
    except:
        return False


def sendKeys(string):
    global driver
    try:
        for chr in string:
            driver.send_keys(str(chr))
        driver.send_keys(Keys.RETURN)
        return True
    except:
        return False


# ---#   Mid Level Actions


def getInfo(user=True):
    getFollowers(user)
    getFollowing(user)


def getFollowers(user=True):
    """
    - if user checking bot followers go to profile else go search user
    find the element that contains the list of followers
    hit tab 31 times to get past first block then log html code
    tabs through until html code no longer updates (all elements cached/ we can now parse data)
    """

    global driver
    if user == True:
        goProfile()
    else:
        goSearch(user)

    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/ul/li[3]/a').click()
    print("before 31 for loop")
    for i in range(31):
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]").send_keys(
            Keys.TAB)
    html_old = driver.page_source
    print("after 31 for loop")
    while True:
        for k in range(6):  # 6 users per block
            for i in range(5):  # tabs through one user profile
                driver.find_element(By.XPATH,
                                    "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]").send_keys(
                    Keys.TAB)
        time.sleep(1)
        if driver.page_source == html_old:
            break
    print("out while loop")  # followers = driver.find_elements(By.XPATH, "")


def getFollowing(user=True):
    global driver
    if user:
        goProfile()
    else:
        goSearch(user)


# ---# High Level Actions


def findGhostFollowers(user=True):
    global driver
    if user:
        pass
    else:
        pass


def findBotFollowers(user=True):
    global driver
    if user:
        pass
    else:
        pass


def findGhostFollowing(user=True):
    global driver
    if user:
        pass
    else:
        pass


def findBotFollowing(user=True):
    global driver
    if user:
        pass
    else:
        pass


def findFollowersNotFollowingBack(user=True):
    global driver
    if user:
        pass
    else:
        pass


def findFollowingNotFollowingBack(user=True):
    global driver
    if user:
        pass
    else:
        pass


def parseBio(bio_element):
    return
