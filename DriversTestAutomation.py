from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import warnings, sys
import phoneNotification as pn

warnings.filterwarnings("ignore", category=DeprecationWarning) 


try:
    usrname = sys.argv[1]
    paswrd = sys.argv[2]

    insta_usrname = sys.argv[3]
    insta_paswrd = sys.argv[4]
    try:
        PATH = sys.argv[5]
    except:
        PATH = r"C:\Users\Ryan1\Downloads\chromedriver_win32\chromedriver.exe" 

except:
    raise Exception("USEAGE: LICENSENUMBER PASSWORD INSTAGRAM_USERNAME INSTAGRAM_PASSWORD PATH_TO_CHROMEDRIVER")
    

options = webdriver.ChromeOptions()

options.add_argument('log-level=3')
driver = webdriver.Chrome(PATH, options=options)

driver.get('https://www.myrta.com/wps/portal/extvp/myrta/licence/tbs/tbs-login/!ut/p/b1/hc_LkpswEAXQb_EHuCRAgFmKtwQEgbFs2FAwFWMYXgYC9nz9eKayyCZJ727XqdvVIAMXkPXFWlfFUg990X7lTMmhazF-ElXhIMkmJLah6kLIBGgI4Pwi6Rf5y2D4_4bsm1BmscB3D0IYHHWIERPj4OhJ4UH8Df5xIn0B9Y8Gor3WyDdiYgaiQ0XA-2HqXv8k4GK_VZo54MrEZeQIVmJveaV0g3FW2PVk0z1uT_K6Tk6MbEOmv9y7cs6220M63H5oftHdXYeWYeG-T1xCochSv28IeayF0bE46boMbsuDb_kdUJCVw_COk5_z4g9V3QPevG2qOZPNxGZ0lxKqBk9uEU-OhLPe-l77iIgvP1lpXHR1mrG6kQArWjg3M1J92PdL4y7GPlWft62lAy-tyxitNUr08HrlmcAkYRTl3G7WWCmhZ1FDnG5N4xfjmFAU5nI0pwTxD69AtTnE49ZDlDuxWNTRbgfGztbIPl07vNt9AkjDlxQ!/')
time.sleep(2)


box = driver.find_element_by_xpath('//*[@id="customerValidationForm"]/div/h2/span')
box.click()
time.sleep(5)


username=driver.find_element_by_xpath('//*[@id="widget_cardNumber"]')
password=driver.find_element_by_xpath('//*[@id="widget_password"]')
username.clear()
password.clear()

#ENTER LOGIN DETAILs 
username.send_keys(usrname)
password.send_keys(paswrd)
time.sleep(1)
password.send_keys(Keys.RETURN)

time.sleep(10)

password=driver.find_element_by_xpath('//*[@id="rms_bat1"]/h2/span')
password.click()
time.sleep(10)
password=driver.find_element_by_xpath('//*[@id="c1tt3"]')
password.click()
time.sleep(3)

password=driver.find_element_by_xpath('//*[@id="nextButton_label"]')
password.click()
time.sleep(10)
password=driver.find_element_by_xpath('//*[@id="checkTerms"]')
password.click()
time.sleep(2)

password=driver.find_element_by_xpath('//*[@id="nextButton_label"]')
password.click()
time.sleep(10)
#after terms
password=driver.find_element_by_xpath('//*[@id="rms_batLocPost"]/h2/span')
password.click()
time.sleep(2)
password=driver.find_element_by_xpath('//*[@id="inputSuburbName"]')
#ENTER YOUR POST CODE
postcode = 2000
password.send_keys(postcode)
time.sleep(5)

password=driver.find_element_by_xpath('//*[@id="inputSuburbName_popup0"]')
password.click()
time.sleep(1)

password=driver.find_element_by_xpath('//*[@id="verifyTestLoc_label"]')
password.click()
time.sleep(2)

password=driver.find_element_by_xpath('//*[@id="rms_searchwell"]/ul/li[1]/label')
password.click()
time.sleep(2)

password=driver.find_element_by_xpath('//*[@id="nextButton_label"]')
password.click()
time.sleep(2)
while True:
    driver.refresh()
    #set the time frequency check for open slot
    time.sleep(60)
    try:
        my_element = driver.find_element_by_xpath("//p[text()='There are no timeslots available at this location.']")
        print("GOT IT")

    except:
        pn.sendmsg("DRIVER TEST AVALIBLE",insta_usrname,insta_paswrd, PATH)
        print("NOT FOUND")


