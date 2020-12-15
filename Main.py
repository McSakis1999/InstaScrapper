import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import datetime
import random
import functions as insta

#Getting username/password from the text files
u = open("info-files\\username.txt", "r")
p = open("info-files\\password.txt", "r")
username = u.read()
password = p.read()
u.close()
p.close()

amount = 11 #ο αριθμος των followers
#x = datetime.datetime.now() Για να κρατας ποτε εκανες καταγραφη
driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\SeleniumP\\chromedriver.exe")
insta.login(username,password,driver)

comment = ""
link = ""
#insta.addcomment(comment,link,1,driver)

ftype = "followers"
follower_list = insta.get_followers(username,ftype,amount,driver)
insta.SaveToCSV(username,follower_list)