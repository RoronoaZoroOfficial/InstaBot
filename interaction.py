import random
import selenium
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC, wait 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.webdriver import WebDriver
import Login

ser = Service("C:\WebDriver\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

Login.login('something_big_coming_soon','As@9719493434',driver)
hashtag = ['Kpop','BTS']
comments = ['Awesome!!!','Looks awesome!','Nice ❤']

class Interaction:
    def __init__(self, hashtag, like, comments, share, driver):
        self.hashtag = hashtag
        self.like = like
        self.comments = comments
        self.share = share
        self.driver = driver
        self.Hashtag()
        self.Like()
        self.Go_right()
        self.Comment()

    def Hashtag(self):
        for i in hashtag:
            driver.get("https://www.instagram.com/explore/tags/"+ i)
            time.sleep(3)
            
            post = driver.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
            post.click()
            time.sleep(4)    
            for i in range(1,5):
                self.Comment()
                self.Go_right() 
                
    def Go_right(self):
        try:
            go_right = driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div/div[2]/button')
            go_right.click()                    
            time.sleep(6)
        except:
            go_right = driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div/div/button')
            go_right.click()
            time.sleep(6)

    def Like(self):
        like = driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
        like.click()
        time.sleep(2)
    
    def Comment(self):
        time.sleep(2)
        commenttext = str(random.choice(comments))
        commentpath = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
        commentpath.click()
        commentpath = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
        # commentpath = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')))
        commentpath.send_keys(commenttext)
        sendcomment = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button[2]')
        sendcomment.click()
        time.sleep(2)

Interaction(hashtag,None, comments, None, driver)