import os
import time
import random
import winsound
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument('--disable-gpu')
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 2 
  })

print("###   A T T E N D A N C E   H A C K   1 0 1   ###\n")
print("Enter Meeting Code: ", end="")
code = input("")
link = "https://meet.google.com/" + code

path = os.getcwd() + '\chromedriver.exe'
def s2r(path):
    return fr"{path}"
chrome_path = s2r(path)

## FIELDS TO EDIT ##

YOUR_EMAIL_ADDRESS = "devarsh@gmail.com" # Replace with your EMAIL ADDRESS
YOUR_PASSWORD = "password" # Replace with your PASSWORD

####################

driver = webdriver.Chrome(options=opt, executable_path=chrome_path)
driver.get('https://accounts.google.com/signin/oauth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3ABBC%2C16%3A9b15b0994c6df9fc%2C10%3A1591711286%2C16%3A66b338ce162d6599%2Ca78a0c663f0beb12c0559379b61a9f5d62868c4fbd2f00e46a86ac26796507a1%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22921f8f04441041069683cc2377152422%22%7D&response_type=code&o2v=1&as=NCQvtBXI4prkLLDbn4Re0w&flowName=GeneralOAuthFlow')

time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(YOUR_EMAIL_ADDRESS)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/span/span').click()

time.sleep(5)
driver.find_element_by_name('password').send_keys(YOUR_PASSWORD)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/span/span').click()

time.sleep(5)
driver.get(link)
time.sleep(15)

# TURNING OFF CAMERA AND MIC

ActionChains(driver).key_down(Keys.CONTROL).send_keys('d').key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).send_keys('e').key_up(Keys.CONTROL).perform()
time.sleep(5)

# CLICKS "JOIN NOW" OR "ASK TO JOIN"
driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]').click()
time.sleep(25)

action = ActionChains(driver)
action.move_by_offset(100, 100).perform()

# CLICKS TURN ON "CAPTIONS"
try:
    driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[9]/div[3]/div[2]/div').click()
    time.sleep(10)
except:
    print("Restart the Script.")
    driver.quit()
    sys.exit()

def letsRunAgain():
    try:
        captionbox = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[5]')
        inside = captionbox.find_element_by_class_name('iTTPOb')
        text = inside.find_elements_by_class_name('CNusmb')
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for x in text:
            string = x.text.lower()
            print(string)
            for pun in string:
                if(pun in punctuations):
                    string = string.replace(pun, "")
            parts = string.split()
            for strx in parts:
                if(strx == "attendance" or strx == "present" or strx == "enrollment"): # You can add your custom words
                    print("\n\n## ATTENDANCE ALERT##\n\n")
                    frequency = 2500
                    duration = 5000 #1000ms = 1sec
                    winsound.Beep(frequency,duration)
    except:
        print("No Text")

while(True):
    time.sleep(2)
    letsRunAgain()