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

ftype = "followers" 

driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\SeleniumP\\chromedriver.exe")
insta.login(username,password,driver)

#Run one of the functions at a time (addcoment or getfollowers)
'''
comment_count = 1   #change it to the number of comments you want to post
link = ""
comment = ""
insta.addcomment(comment,link,comment_count,driver)

'''
follower_count = 1  #change it to your number of followers
follower_list = insta.get_followers(username,ftype,follower_count,driver)
result = insta.SaveToCSV(username,follower_list)
print(result)

driver.close()