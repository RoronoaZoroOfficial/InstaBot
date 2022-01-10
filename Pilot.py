from contextlib import nullcontext
import os
from time import sleep
from tkinter import Frame, Label, Scrollbar, font
from tkinter.constants import ANCHOR, END, RIGHT, S, VERTICAL, Y
from typing import Annotated
from typing_extensions import IntVar
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
from interaction import Interaction
import tkinter as tk
from apscheduler.schedulers.background import BackgroundScheduler

#####################################################################
# Login.login('something_big_coming_soon','As@9719493434',driver)
target = ['BTS','agustd','rkive']
comments = ['Awesome!!!','lit 🔥','Nice ❤']

#####################################################################
# follow.followers(target, driver)
# class SchedulerObject:
#     def __init__(self, username, password):
#         self.username = username.get()
#         self.password = password.get()


class MainApplication(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.gui = self.configure_gui
        self.widgets = self.create_widgets()
        self.scheduleObjects = []
        self.Hashtag = []
        self.Comment = []
        self.Pages = []
        self.driver = webdriver.Chrome(service=ser, options=op)


    def configure_gui(self):
        tk.Tk.geometry(self,"1200x720+30+20")

    def create_widgets(self):
        # scheduleRun = tk.Button(self.master, text= 'Schedule', padx=300, pady= 50, bg= '#c38a4d', fg='#fff', command=self.Task)
        # scheduleRun.pack()

        #Login GUI
        self.login_frame = tk.LabelFrame(self.master,text='Login',pady=20,padx=30)
        self.login_frame.grid(column=0, row=0, padx=30, pady=20)
        self.UsernameLabel = tk.Label(self.login_frame, text= 'Username',font=("Arial",18),pady=7,padx=10)
        self.UsernameLabel.grid(column=0, row=0)

        self.UsernameEntry = tk.Entry(self.login_frame, font=("Arial",18))
        self.UsernameEntry.grid(column=1, row=0,pady=7,padx=10)
        self.usernametxt = tk.StringVar() 
        self.usernametxt.set('')
        self.usernametxt = self.UsernameEntry

        self.PasswordLabel = tk.Label(self.login_frame, text='Password', font=("Arial",18))
        self.PasswordLabel.grid(column=0, row=1,pady=7,padx=10) 

        self.PasswordEntry = tk.Entry(self.login_frame, font=("Arial",18))
        self.PasswordEntry.grid(column=1, row=1,pady=7,padx=10)
        self.passwordtxt = tk.StringVar()
        self.passwordtxt.set('')
        self.passwordtxt = self.PasswordEntry

        self.GUI_login = tk.Button(self.login_frame, text= 'Login', padx=30, pady= 10, bg= '#b4b4b4', fg='#000', command=self.signin, width=20)
        self.GUI_login.grid(column=0, row=3,pady=7,padx=10,columnspan=2)

        #Hash tags GUI
        self.HT_frame = tk.LabelFrame(self.master,text='Interaction',pady=50,padx=30)
        self.HT_frame.grid(column=1, row=0)
        self.HashtagLabel = tk.Label(self.HT_frame, text= 'Hashtag', font=("Arial",18))
        self.HashtagLabel.grid(column=0, row=0) 
        self.HashtagEntry = tk.Entry(self.HT_frame, font=("Arial",18))
        self.HashtagEntry.grid(column=1, row=0)
        self.Hashtagtxt = tk.StringVar()
        self.Hashtagtxt.set('')
        self.Hashtagtxt = self.HashtagEntry

        self.Hashtag_Add = tk.Button(self.HT_frame,text= "Add Hashtag", padx= 10, pady= 5, bg="#4e4e4e", fg= "#fff",command= self.addhashtag , font=("Arial",18))
        self.Hashtag_Add.grid(column=0, row=1)
        self.Hashtag_Remove = tk.Button(self.HT_frame,text= "Remove Hashtag", padx= 10, pady= 5, bg="#4e4e4e", fg= "#fff",command= self.removehashtag , font=("Arial",18))
        self.Hashtag_Remove.grid(column=0, row=2)
        
        self.LB_HT_Frame = tk.Frame(self.HT_frame)
        self.LB_HT_Frame.grid(column=1, row=1,padx= 10, pady= 5, rowspan=2)
        self.LB_HT_scroll = tk.Scrollbar(self.LB_HT_Frame,orient=VERTICAL)
        
        self.LB_HT = tk.Listbox(self.LB_HT_Frame,height=6, font=("Arial",18), yscrollcommand= self.LB_HT_scroll.set)
        self.LB_HT_scroll.config(command=self.LB_HT.yview)
        self.LB_HT_scroll.pack(side=RIGHT, fill=Y)
        self.LB_HT.pack()

        self.likelabel = tk.Label(self.HT_frame, text='Like Count', font=("Arial",18))
        self.likelabel.grid(column=0, row=3)
        self.likecount = tk.Spinbox(self.HT_frame, from_=0, to= 10, font=("Arial",18))
        self.likecount.grid(column=1, row=3)  
        
        self.commentlabel = tk.Label(self.HT_frame, text='Comment Count', font=("Arial",18))
        self.commentlabel.grid(column=0, row=4)
        self.commentcount = tk.Spinbox(self.HT_frame, from_=0, to= 10, font=("Arial",18))
        self.commentcount.grid(column=1, row=4)

        self.sharelabel = tk.Label(self.HT_frame, text='Share Count', font=("Arial",18))
        self.sharelabel.grid(column=0, row=5)
        self.sharecount = tk.Spinbox(self.HT_frame, from_=0, to= 10, font=("Arial",18))
        self.sharecount.grid(column=1, row=5)

        self.share_amount_label = tk.Label(self.HT_frame, text='Share Count', font=("Arial",18))
        self.share_amount_label.grid(column=0, row=6)
        self.share_amount = tk.Spinbox(self.HT_frame, from_=0, to= 10, font=("Arial",18))
        self.share_amount.grid(column=1, row=6)

        self.CommentLabel = tk.Label(self.HT_frame, text= 'Comment', font=("Arial",18))
        self.CommentLabel.grid(column=0, row=7) 
        self.CommentEntry = tk.Entry(self.HT_frame, font=("Arial",18))
        self.CommentEntry.grid(column=1, row=7)
        self.Commenttxt = tk.StringVar()
        self.Commenttxt.set('')
        self.Commenttxt = self.HashtagEntry

        self.Comment_Add = tk.Button(self.HT_frame,text= "Add Comment", padx= 10, pady= 5, bg="#4e4e4e", fg= "#fff",command= self.addcomment , font=("Arial",18))
        self.Comment_Add.grid(column=0, row=8)
        self.Comment_Remove = tk.Button(self.HT_frame,text= "Remove Comment", padx= 10, pady= 5, bg="#4e4e4e", fg= "#fff",command= self.removecomment , font=("Arial",18))
        self.Comment_Remove.grid(column=0, row=9)
        
        self.LB_comment_Frame = tk.Frame(self.HT_frame)
        self.LB_comment_Frame.grid(column=1, row=8, padx= 10, pady= 5, rowspan=2)
        self.LB_comment_scroll = tk.Scrollbar(self.LB_comment_Frame,orient=VERTICAL)
        
        self.LB_comment = tk.Listbox(self.LB_comment_Frame,height=6, font=("Arial",18), yscrollcommand= self.LB_comment_scroll.set)
        self.LB_comment_scroll.config(command=self.LB_comment.yview)
        self.LB_comment_scroll.pack(side=RIGHT, fill=Y)
        self.LB_comment.pack()

        
        self.likevar = tk.IntVar()
        self.like = tk.Checkbutton(self.HT_frame, text='Like', variable=self.likevar, font=("Arial",18))
        self.like.deselect()
        self.like.grid(column=0, row=10)
        
        self.commentvar = tk.IntVar()
        self.comment = tk.Checkbutton(self.HT_frame, text='Comment', variable=self.commentvar, font=("Arial",18))
        self.comment.deselect()
        self.comment.grid(column=1, row=10)
        
        self.sharevar = tk.IntVar()
        self.share = tk.Checkbutton(self.HT_frame, text='Share', variable=self.sharevar, font=("Arial",18))
        self.share.deselect()
        self.share.grid(column=0, row=11)

        self.validate = tk.Button(self.HT_frame,command=self.interaction,text="validate", font=("Arial",18))
        self.validate.grid(column=1, row=11)

        #Pages List GUI
        self.Page_frame = tk.LabelFrame(self.master,text='Steal Followers')
        self.Page_frame.grid(column=2, row=0)
        self.PagesLabel = tk.Label(self.Page_frame, text = 'Pages', font=("Arial",18))
        self.PagesLabel.grid(column=0, row=0) 
        self.PagesEntry = tk.Entry(self.Page_frame, width=20, font=("Arial",18))
        self.PagesEntry.grid(column=1, row=0)
        self.Pagestxt = tk.StringVar()
        self.Pagestxt.set('')
        self.Pagestxt = self.PagesEntry

        self.Pages_Add = tk.Button(self.Page_frame,text= "Add Page", padx= 10, pady= 5, bg="#4e4e4e", fg= "#fff", command= self.addpages , font=("Arial",18))
        self.Pages_Add.grid(column=0, row=1)
        self.Pages_Remove = tk.Button(self.Page_frame,text= "Remove Page", padx= 10, pady= 5, bg="#4e4e4e", fg= "#fff",command= self.removepages , font=("Arial",18))
        self.Pages_Remove.grid(column=0, row=2)
        
        self.LB_P_Frame = tk.Frame(self.Page_frame)
        self.LB_P_Frame.grid(column=1, row=1,padx= 10, pady= 5, rowspan=2)
        self.LB_P_scroll = tk.Scrollbar(self.LB_P_Frame,orient=VERTICAL)
        self.LB_P = tk.Listbox(self.LB_P_Frame,height=5, font=("Arial",18))
        self.LB_P_scroll.config(command=self.LB_P.yview)
        self.LB_P_scroll.pack(side=RIGHT, fill=Y)
        self.LB_P.pack()

        
        self.followlabel = tk.Label(self.Page_frame, text='Follow Count', font=("Arial",18))
        self.followlabel.grid(column=0, row=3)
        self.followcount = tk.Spinbox(self.Page_frame, from_=1, to= 12, font=("Arial",18))
        self.followcount.grid(column=1, row=3)
        
        self.followtimelabel = tk.Label(self.Page_frame, text='Time interval/follow (sec)', font=("Arial",18))
        self.followtimelabel.grid(column=0, row=4)
        self.followtimecount = tk.Spinbox(self.Page_frame, from_=2, to= 10, font=("Arial",18))
        self.followtimecount.grid(column=1, row=4)

        self.pagetimelabel = tk.Label(self.Page_frame, text='Time interval/Page (sec)', font=("Arial",18))
        self.pagetimelabel.grid(column=0, row=5)
        self.pagetimecount = tk.Spinbox(self.Page_frame, from_=5, to= 10, font=("Arial",18))
        self.pagetimecount.grid(column=1, row=5)

        self.Hack_btn = tk.Button(self.Page_frame,text= "Hack", padx= 10, pady= 5, bg="#4e4e4e", fg= "#fff", command= self.hack , font=("Arial",18))
        self.Hack_btn.grid(column=0, row=6)
        self.unfollow_btn = tk.Button(self.Page_frame,text= "Unfollow", padx= 10, pady= 5, bg="#4e4e4e", fg= "#fff", command= self.unfollow , font=("Arial",18))
        self.unfollow_btn.grid(column=1, row=6)
        
        return self.UsernameEntry, self.PasswordEntry , self.HashtagEntry , self.PagesEntry, self.CommentEntry

    def signin(self):
        username, password, x, y,z = self.widgets
        id = username.get()
        pwd = password.get()
        Login.login(id, pwd, self.driver)
        sleep(10)
        print(id, pwd)
    
    def addhashtag(self):
        x,y, ht, z ,w= self.widgets
        newHashtag = ht.get()
        self.Hashtag.append(newHashtag)
        self.LB_HT.insert(END, newHashtag)
        self.HashtagEntry.delete(0, END)
    
    def removehashtag(self):
        self.Hashtag.remove(self.LB_HT.get(ANCHOR))
        self.LB_HT.delete(ANCHOR)

    def addcomment(self):
        x,y, w, z, cmnt = self.widgets
        print(cmnt)
        newComment = cmnt.get()
        self.Comment.append(newComment)
        self.LB_comment.insert(END, newComment)
        self.CommentEntry.delete(0, END)
    
    def removecomment(self):
        self.Comment.remove(self.LB_comment.get(ANCHOR))
        self.LB_comment.delete(ANCHOR)

    def addpages(self):
        x,y, z, pg , w= self.widgets
        newPage = pg.get()
        self.Pages.append(newPage)
        self.LB_P.insert(END, newPage)
        self.PagesEntry.delete(0, END)
    
    def removepages(self):
        self.Pages.remove(self.LB_P.get(ANCHOR))
        self.LB_P.delete(ANCHOR)        

    def interaction(self):
        self.like_var = self.likevar.get()
        self.comment_var = self.commentvar.get()
        self.share_var =  self.sharevar.get()
        if self.like_var == 0 and self.comment_var == 0 and self.share_var == 0:
            Popup = tk.Label(self.HT_frame, text='Please Select checkbox(s)', font=("Arial",18))
            Popup.grid(column=0,row=12)
            return
        else:
            Interaction.Hashtag(self,self.Hashtag, self.driver)
            total_count = [int(self.likecount.get()),int(self.commentcount.get()),int(self.sharecount.get())]
            total_count.sort()
            l_count = int(0)
            c_count = int(0)
            s_count = int(0)
            for i in range(1,total_count[-1]):
                if self.like_var == 1:
                    self.likevalue = Interaction.Like(self,self.driver,int(self.likecount.get()),l_count,self.likevar)
                    self.like_var, l_count = self.likevalue
                
                if self.comment_var == 1:
                    self.commentvalue = Interaction.Comment(self,self.Comment,int(self.commentcount.get()), self.driver,c_count,self.commentvar)
                    self.comment_var, c_count = self.commentvalue
                    
                if self.share_var == 1:
                    self.sharevalue = Interaction.Share(self,int(self.sharecount.get()),int(self.share_amount.get()),self.driver,s_count,self.sharevar)
                    self.share_var , s_count = self.sharevalue
                    
                Interaction.Go_right(self,self.driver)
                
                    
    def hack(self):
        print(self.Pages)
        print(self.followcount.get())
        print(self.followtimecount.get())
        print(self.pagetimecount.get())
        

    def unfollow(self):
        follow.FollowActions.unfollow(self,self.driver)
    


if __name__ == '__main__':
    root = tk.Tk()
    root.title = "GUI"
    ser = Service("C:\WebDriver\chromedriver_win32\chromedriver.exe")
    op = webdriver.ChromeOptions()
    main_app = MainApplication(root)
    root.mainloop()


