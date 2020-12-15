import selenium
from selenium import webdriver
import functions as insta

#Getting username/password from the text files
u = open("info-files\\username.txt", "r")
p = open("info-files\\password.txt", "r")
username = u.read()
password = p.read()
u.close()
p.close()

amount = 5 #ο αριθμος των followers
#x = datetime.datetime.now() Για να κρατας ποτε εκανες καταγραφη
driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\SeleniumP\\chromedriver.exe")
insta.login(username,password,driver)

comment = ""
link = ""
#insta.addcomment(comment,link,1,driver)

ftype = "followers"
follower_list = insta.get_followers(username,ftype,amount,driver)
result = insta.SaveToCSV(username,follower_list)
print(result)