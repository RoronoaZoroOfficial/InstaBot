from contextlib import nullcontext
from os import scandir
from time import sleep
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import by
from selenium.webdriver.common import touch_actions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.remote.webelement import isDisplayed_js
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC, wait 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import common
import time
import pickle
import Login


# Follow---------------------------------------------------

# page = ["kpopindiamerch"]
# page = ["agustd"]
# page = ["rkive"]
def followers(page, driver):
    for x in page:     
        driver.get('https://www.instagram.com/' + x)
        driver.implicitly_wait(7,11)

        followerCount = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
        FC = followerCount.get_attribute("title")
        FC = FC.replace(',','')
        follow_counter = int(float(FC))

        followerCount.click()
        driver.implicitly_wait(5)

        count= 0 #count in one cycle
        n=0 #number of cycle
        # scroll = driver.find_element(By.XPATH, '/html/body/div[6]/div')

        for i in range(1,12):
            try:
                follow = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]/ul/div/li[' + str(i) +']/div/div[3]/button')
                follow.click()
            except NoSuchElementException:
                pass
            driver.implicitly_wait(5,9)

            try:
                cancel = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel.click()
            except NoSuchElementException:
                pass

        