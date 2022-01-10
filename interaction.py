from os import close
import random
from tkinter.constants import TOP
from typing_extensions import IntVar
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
        self.Share()

    def Hashtag(self,hashtag,driver):
        for i in hashtag:
            driver.get("https://www.instagram.com/explore/tags/"+ i)
            time.sleep(3)
            
            post = driver.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
            post.click()
            time.sleep(4)    
                
    def Go_right(self,driver):
        try:
            go_right = driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div/div[2]/button')
            go_right.click()                    
            time.sleep(3)
        except:
            go_right = driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div/div/button')
            go_right.click()
            time.sleep(3)

    def Like(self,driver,like_count,l_count,likevalue):
        like_count = int(like_count)
        if l_count < like_count:
            like = driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
            like.click()
            time.sleep(2)
            l_count += int(1)
            likevalue = int(1)
        else:
            likevalue = int(0)
        return likevalue , l_count
    
    def Comment(self,comments,comment_count,driver,c_c,commentvalue):
        time.sleep(2)
        comment_count = int(comment_count)
        if c_c >= comment_count:
            commentvalue = int(0)
        elif c_c < comment_count:
            commenttext = str(random.choice(comments))
            commentpath = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
            commentpath.click()
            time.sleep(2)
            commentpath = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
            commentpath.send_keys(commenttext)
            sendcomment = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button[2]')
            sendcomment.click()
            c_c += c_c + int(1)
            commentvalue = int(1)
            time.sleep(2)
        return commentvalue , c_c
        

    def Share(self,share_count,share_amount,driver,s_count,sharevalue):
        time.sleep(2)
        share_count = int(share_count)
        share_amount = int(share_amount)
        if s_count < share_count:
            share = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[3]/button')
            share.click()
            for i in range(0,share_amount):
                share_to = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div[2]/div[2]/div['+ i +']/div/div[3]/button')
                share_to.click()
                time.sleep(3)
            s_count += int(1)
            close = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div[1]/div/div[2]/div/button')
            close.click()
            sharevalue = int(1)
        else:
            sharevalue = (0)
        return sharevalue , s_count