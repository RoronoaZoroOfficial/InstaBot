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

# ser = Service("C:\WebDriver\chromedriver_win32\chromedriver.exe")
# op = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=ser, options=op)

# Login.login('something_big_coming_soon','As@9719493434',driver)
# Follow---------------------------------------------------

# page = ["kpopindiamerch"]
# page = ["agustd"]
# page = ["rkive"]
class FollowActions:
    def __init__(self,page,driver):
        self.page = page
        self.driver = driver
        self.followers()
        self.unfollow()

    def followers(self, page, driver):
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

    def unfollow(self,driver):
        driver.get('https://www.instagram.com/'+ 'something_big_coming_soon')
        time.sleep(2)
        following = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
        following.click()
        WebDriver.implicitly_wait(driver,5)
        for i in range(1,12):
            try:
                unfollow = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[3]/ul/div/li[' + str(i) +']/div/div[3]/button')
                unfollow.click()
            except NoSuchElementException:
                pass
            

            try:
                cancel = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[1]')
                cancel.click()
                time.sleep(5)
            except NoSuchElementException:
                pass

