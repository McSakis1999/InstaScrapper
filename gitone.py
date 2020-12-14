from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import time
import os
import datetime

count = 100  # number of profiles you want to get
 # account from
page = "followers"  # from following or followers

u = open("info-files\\username.txt", "r")
p = open("info-files\\password.txt", "r")
yourusername = u.read()
yourpassword = p.read()
u.close()
p.close()



#for proxy i recommend 4G mobile proxy: http://www.virtnumber.com/mobile-proxy-4g.php
#PROXY = "http://84.52.54.2:8011" # IP:PORT or HOST:PORT
#options.add_argument('--proxy-server=%s' % PROXY)

driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\Selenium Project\\chromedriver.exe")
driver.get('https://www.instagram.com/accounts/login/')
sleep(3)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Αποδοχή')]"))).click()
sleep(1)
username_input = driver.find_element_by_css_selector("input[name='username']")
password_input = driver.find_element_by_css_selector("input[name='password']")
username_input.send_keys(yourusername)
password_input.send_keys(yourpassword)
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
sleep(2) 
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Όχι τώρα')]"))).click()
sleep(3)
driver.get("https://www.instagram.com/"+yourusername)
sleep(2) 
driver.find_element_by_xpath('//a[contains(@href, "%s")]' % page).click()
scr2 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
sleep(2)
text1 = scr2.text
print(text1)
x = datetime.datetime.now()
print(x)

for i in range(1,count):
   scr1 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[%s]' % i)
   driver.execute_script("arguments[0].scrollIntoView();", scr1)
   sleep(1)
   text = scr1.text
   fol_list = text.encode('utf-8').split()
   print('{};{}'.format(i, fol_list[0]))
   #print(i + ";" + list[0])
   if i == (count-1):
     print(x)