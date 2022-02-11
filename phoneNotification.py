from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def sendmsg(text):
    #enter path to chrome driver where ever you download it to
    PATH = r"C:\Users\Downloads\chromedriver_win32\chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(PATH, options=options)

    driver.get('https://www.instagram.com')


    time.sleep(5)
    username=driver.find_element_by_css_selector("input[name='username']")
    password=driver.find_element_by_css_selector("input[name='password']")
    username.clear()  
    password.clear()
    #enter instagram username and password
    username = "kkkkk"
    passwd = "jjjjjj"
    username.send_keys(username)
    password.send_keys(passwd)
    password.send_keys(Keys.RETURN)

    time.sleep(5)
    notification = driver.find_element_by_css_selector('[class="aOOlW   HoLwm " ]')
    notification.click()
    time.sleep(0.5)

    dms = driver.find_element_by_css_selector('[aria-label="Messenger"]')
    dms.click()
    time.sleep(4)

    people = driver.find_elements_by_css_selector('[class="-qQT3 rOtsg"]')
    #uses the most recent person in the direct messeges
    people[0].click()

    time.sleep(3)
    textboxinsta = driver.find_element_by_css_selector('[placeholder="Message..."]')
    time.sleep(1)
    textboxinsta.send_keys(text)
    textboxinsta.send_keys(" ", Keys.ENTER)