import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep 
import csv
import datetime
import random

def login(username, password, driver):
    driver.get("https://www.instagram.com/accounts/login/")
    count = 0
    while count < 20:
    	try:
    		username_element = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/form/div/div[1]/div/label/input')
    		password_element = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/form/div/div[2]/div/label/input')
    		break
    	except:
    		sleep(1)
    		count = count + 1
    		print(count)
    #
    #change Αποδοχη το Accept <------
    #
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Αποδοχή')]"))).click()
    username_element.send_keys(username)
    password_element.send_keys(password)
    sleep(1)
    login_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/form/div/div[3]/button')
    login_button.click()
    sleep(4)

def get_followers(username,ftype,amount,driver):
    #
    #Change Οχι τωρα to Not Now <------
    #
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Όχι τώρα')]"))).click()
    sleep(3)
    driver.get("https://www.instagram.com/"+username)
    sleep(2)
    driver.find_element_by_xpath('//a[contains(@href, "%s")]' % ftype).click()
    scr2 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    sleep(2)
    text1 = scr2.text
    print(text1)
    final_fol_list = []
    for i in range(1,amount+1):
        scr1 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[%s]' % i)
        driver.execute_script("arguments[0].scrollIntoView();", scr1)
        sleep(1)
        text = scr1.text
        fol_list = text.encode('utf-8').split()
        accname = str(fol_list[0])
        final_fol_list.append((i,accname[2:len(accname)-1]))
    return final_fol_list

def addcomment(comment,link,number,driver):
    driver.get(link)
    sleep(3)
    comment_number = 0
    random_delay = random.randint(40,50)
    while comment_number <= number:
        commentArea = driver.find_element_by_class_name('Ypffh')
        commentArea.click()
        commentArea = driver.find_element_by_class_name('Ypffh')
        commentArea.send_keys(comment)
        #
        #Change Δημοσιευση to Comment  <------
        #
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Δημοσίευση')]"))).click()
        #Button = driver.find_element_by_xpath('/html/body/div/section/main/div/div/article/div[3]/section[3]/div/form/button').click()
        comment_number+=1
        print(comment_number)
        sleep(random_delay)

def SaveToCSV(username,entry):
    csv_name = "saved-data//"+username+".csv"
    creation_date = datetime.datetime.now()
    fields = ['Id','Username',str(creation_date)]
    rows = entry 
    try:
        f = open(csv_name, 'r')
        result = find_unfollowers(csv_name,entry,f)
        f.close()
        with open(csv_name, 'w') as f:
            write = csv.writer(f ,lineterminator ='\n') 
            write.writerow(fields) 
            write.writerows(rows)
        f.close()
        return result
    except FileNotFoundError:
        with open(csv_name, 'w') as f:
            write = csv.writer(f ,lineterminator ='\n') 
            write.writerow(fields) 
            write.writerows(rows)
        f.close()
        result = []
        return result
    

def find_unfollowers(csv_name,follower_list,file):
    f = file
    old_csv = csv.reader(f)
    next(old_csv)
 
    old_list = []
    for line in old_csv:
        old_list.append(line[1]) 

    new_list = []
    for item in follower_list:
        new_list.append(item[1])
    unfollowers = list(set(old_list) - set(new_list))
    return unfollowers

