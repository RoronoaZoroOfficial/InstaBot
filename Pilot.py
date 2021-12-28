from contextlib import nullcontext
import os
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
import follow
import interaction
import tkinter as tk
from apscheduler.schedulers.background import BackgroundScheduler

ser = Service("C:\WebDriver\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
actions= ActionChains(driver)
touch= TouchActions(driver)

#####################################################################
# Login.login('something_big_coming_soon','As@9719493434',driver)
target = ['BTS','agustd','rkive']
comments = ['Awesome!!!','lit 🔥','Nice ❤']

#####################################################################
# follow.followers(target, driver)
class SchedulerObject:
    def __init__(self, username, password):
        self.username = username.get()
        self.password = password.get()


class MainApplication(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.gui = self.configure_gui
        self.widgets = self.create_widgets()
        self.scheduleObjects = []

    def configure_gui(self):
        tk.Tk.geometry(self,"1200x720+30+20")

    def create_widgets(self):
        # scheduleRun = tk.Button(self.master, text= 'Schedule', padx=300, pady= 50, bg= '#c38a4d', fg='#fff', command=self.Task)
        # scheduleRun.grid(column=3, row=5, padx=10, pady=15)

        self.UsernameLabel = tk.Label(self.master, text= 'Username', font=16)
        self.UsernameLabel.grid(column= 0, row = 0, padx=10, pady=15) 

        self.UsernameEntry = tk.Entry(self.master, width=20, font=16)
        self.UsernameEntry.grid(column= 1, row = 0, padx=10, pady=15)
        self.usernametxt = tk.StringVar() 
        self.usernametxt.set('')
        self.usernametxt = self.UsernameEntry

        self.PasswordLabel = tk.Label(self.master, textvariable='Pass', font=16)
        self.PasswordLabel.grid(column= 0, row = 1, padx=10, pady=15) 

        self.PasswordEntry = tk.Entry(self.master, width=20, font=16)
        self.PasswordEntry.grid(column= 1, row = 1, padx=10, pady=15)
        self.passwordtxt = tk.StringVar()
        self.passwordtxt.set('')
        self.passwordtxt = self.PasswordEntry

        GUI_login = tk.Button(self.master, text= 'Login', padx=30, pady= 50, bg= '#e413f1', fg='#fff', command=self.signin)
        GUI_login.grid(column=3, row=5, padx=10, pady=15)

        # UsernameLabel = tk.Label(self.master, text= 'Username', font=16)
        # UsernameLabel.grid(column= 0, row = 0, padx=10, pady=15) 

        # UsernameEntry = tk.Entry(self.master, width=20, font=16)
        # UsernameEntry.grid(column= 1, row = 0, padx=10, pady=15)
        return self.UsernameEntry, self.PasswordEntry


    def signin(self):
        username, password = self.widgets
        id = username.get()
        pwd = password.get()
        Login.login(id, pwd, driver)
        sleep(10)
        print(id, pwd)




if __name__ == '__main__':
    root = tk.Tk()
    root.title = "GUI"
    main_app = MainApplication(root)
    root.mainloop()


