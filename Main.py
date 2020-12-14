import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import datetime
import random
#username_element = driver.find_element_by_xpath('/html/body/div[0]/section/main/div/div/div/div/form/div/div[0]/div/label/input')

def login(username, password, driver):
    driver.get("https://www.instagram.com/accounts/login/")
    count = 0
    while count < 20:
    	try:
    		username_element = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/form/div/div[1]/div/label/input')
    		password_element = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/form/div/div[2]/div/label/input')
    		break
    	except:
    		time.sleep(1)
    		count = count + 1
    		print(count)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Αποδοχή')]"))).click()
    username_element.send_keys(username)
    password_element.send_keys(password)
    time.sleep(1)
    login_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/form/div/div[3]/button')
    login_button.click()
    time.sleep(5)

def get_followers(username,amount,driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Όχι τώρα')]"))).click()
    time.sleep(3)
    driver.get("https://www.instagram.com/"+username)
    time.sleep(2)
    driver.find_element_by_xpath('//a[contains(@href, "%s")]' % page).click()
    
    #Για να βρισκει και να τυπωνει ποσους συνολικους followers εχεις
    scr2 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    time.sleep(2)
    text1 = scr2.text
    print(text1)
    
    for i in range(1,amount+1):
        scr1 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[%s]' % i)
        driver.execute_script("arguments[0].scrollIntoView();", scr1)
        time.sleep(1)
        text = scr1.text
        fol_list = text.encode('utf-8').split()
        print('{};{}'.format(i, fol_list[0]))
        #print(i + ";" + list[0])
       

def addcomment(comment,link,number):
    driver.get(link)
    time.sleep(3)
    comment_number = 0
    random_delay = random.randint(40,50)
    while comment_number <= number:
        commentArea = driver.find_element_by_class_name('Ypffh')
        commentArea.click()
        commentArea = driver.find_element_by_class_name('Ypffh')
        commentArea.send_keys(comment)
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Δημοσίευση')]"))).click()
        #Button = driver.find_element_by_xpath('/html/body/div/section/main/div/div/article/div[3]/section[3]/div/form/button')
        #Button.click()

        comment_number+=1
        print(comment_number)
        time.sleep(random_delay)


#Getting username/password from the text files
u = open("info-files\\username.txt", "r")
p = open("info-files\\password.txt", "r")
username = u.read()
password = p.read()
u.close()
p.close()

page = "followers" #followers/following
amount = 10 #ο αριθμος των followers
#x = datetime.datetime.now() Για να κρατας ποτε εκανες καταγραφη
driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\Selenium Project\\chromedriver.exe")
login(username,password,driver)

#link = "https://www.instagram.com/p/CIlA_HesOQz/"
#link = "https://www.instagram.com/p/CIQiZcVFzUq/"
#touni
#link = "https://www.instagram.com/p/CIWEkK0rCIa/"
#soyla glam
#link = "https://www.instagram.com/p/CIc17D_pJ9s/"
#comment = "@sakis_mtsk @vasilistripleog @alex_mitsios"
comment = "hey handsome!"
link = "https://www.instagram.com/p/BQ_V5I2F3XvPhjn4AJncHF1qJva7n4uBk1KCnA0/"
addcomment(comment,link,10)

#commentbox = driver.find_element_by_xpath('/html/body/div/section/main/div/div/article/div[3]/section[3]/div/form/textarea')
#commentbox.send_keys('@sakis_mtsk @mouleva @dora_ts')

#get_followers(username,amount,driver)