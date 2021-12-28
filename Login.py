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


def login(uname, pwd, driver):
    driver.get('https://www.instagram.com/')
    try:
        cookies = pickle.load(open("cookies.pkl","rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get('https://www.instagram.com/')
        sleep(10)
    except:
        Username = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.NAME, 'username')))
        Password = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.NAME, 'password')))
        Username.send_keys(str(uname))
        Password.send_keys(str(pwd))
        login = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
        login.click()
        sleep(10)
        pickle.dump (driver.get_cookies(), open("cookies.pkl","wb"))