import selenium
from selenium import webdriver
import functions as insta
import tkinter as tk

def EntriesFilled(*args):
    user = var1.get()
    pasw = var2.get()
    link = var3.get()
    comm = var4.get()
    comn = var5.get()
    amnt = var6.get()
    if user and pasw:
        Login_btn.config(state="normal")
    else:
        Login_btn.config(state="disabled")
    if link and comm and comn:
        submitbtn.config(state="normal")
    else:
        submitbtn.config(state="disabled")
    if amnt:
        Unfollowers_button.config(state="normal")
    else:
        Unfollowers_button.config(state="disabled")

def SubmitAction():
    global link
    global comment
    global com_number
    link = Elink.get()
    comment = Ecomment.get()
    com_number = commentnumber.get()
    Elink.delete(0, tk.END)
    Ecomment.delete(0, tk.END)    
    commentnumber.delete(0, tk.END)
    insta.addcomment(comment,link,int(com_number),driver)

def Login():
    global username
    global password
    global driver
    username = Eusername.get()
    password = Epassword.get()
    Eusername.delete(0, tk.END)
    Epassword.delete(0, tk.END)
    Eusername.config(state='disabled')
    Epassword.config(state='disabled')
    Elink.config(state='normal')
    Ecomment.configure(state='normal')
    commentnumber.config(state='normal')
    Eamount.config(state="normal")
    driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\SeleniumP\\chromedriver.exe")
    insta.login(username,password,driver)

def Unfollowed():
    global amount
    amount = int(Eamount.get())
    Eamount.delete(0, tk.END)
    fol_list = insta.get_followers(username,"followers",amount,driver)
    unfollowers = insta.SaveToCSV(username,fol_list)
    
global unfollowers
unfollowers = []
root = tk.Tk()
root.title("InstaBot")
root.geometry("700x300+500+200")
root.resizable(0, 0)

#frame 1 --------------------------------- 


var1 = tk.StringVar(root)
var2 = tk.StringVar(root)
var3 = tk.StringVar(root)
var4 = tk.StringVar(root)
var5 = tk.StringVar(root)
var6 = tk.StringVar(root)

var1.trace("w", EntriesFilled)
var2.trace("w", EntriesFilled)
var3.trace("w", EntriesFilled)
var4.trace("w", EntriesFilled)
var5.trace("w", EntriesFilled)
var6.trace("w", EntriesFilled)

frame1 = tk.LabelFrame(root,padx=5,pady=5)
frame1.grid(row=0,column=0,sticky="nsew")

frame2 = tk.LabelFrame(root,padx=5,pady=5)
frame2.grid(row=0,column=1,sticky="nsew")

Login_btn = tk.Button(frame1,text="Log In",padx=10,command = Login)
Login_btn.grid(row=2,columnspan=2)


submitbtn = tk.Button(frame1,text="Submit",command = SubmitAction)
submitbtn.grid(row=6,columnspan=3,pady=1,ipady=3,ipadx=5)

Unfollowers_button = tk.Button(frame2,text="Search",width=15,command=Unfollowed)
Unfollowers_button.grid(row=1,column=6,ipady=5,ipadx=3,pady=20)

Eusername = tk.Entry(frame1,width=20,textvariable=var1)
Eusername.grid(row=1,column=0,padx=5,pady=10,ipady=5,ipadx=5)
Eusername.insert(0,"Enter your username")

Epassword = tk.Entry(frame1,width=20,textvariable=var2)
Epassword.grid(row=1,column=1,padx=5,pady=10,ipady=5,ipadx=5)
Epassword.insert(1,"Enter your password")

Elink = tk.Entry(frame1,width=50,textvariable=var3)
Elink.grid(row=3,columnspan=3,padx=5,pady=10,ipady=5,ipadx=5)
Elink.insert(1,"Enter the post's link")
Elink.configure(state='disabled')

Ecomment = tk.Entry(frame1,width=50,textvariable=var4)
Ecomment.grid(row=4,columnspan=3,padx=5,pady=10,ipady=5,ipadx=5)
Ecomment.insert(2,"Type your comment")
Ecomment.configure(state='disabled')

commentnumber = tk.Entry(frame1,width=22,textvariable=var5)
commentnumber.grid(row=5,columnspan=3,padx=5,pady=10,ipady=5,ipadx=5)
commentnumber.insert(2,"Number of comments")
commentnumber.configure(state='disabled')


timelabel = tk.Label(frame1 ,text="The estimated time is :")
timelabel.grid(row=7,columnspan=3,ipady=10,pady=5)

#frame 2 ---------------------------------------------------


frame2label = tk.Label(frame2, text="Find out who unfollowed you!", font='Helvetica 12 bold')
frame2label.grid(row=0,column=4,columnspan=4)

Eamount = tk.Entry(frame2,width=15,textvariable=var6)
Eamount.grid(row=1,column=5,pady=5,ipady=6,)
Eamount.insert(2,"Follower Count")
Eamount.configure(state='disabled')


#frame 3 inside 2 ^^^^^^^^^^^^^^^^^^^^^^^^^^

frame3 = tk.LabelFrame(frame2)
frame3.grid(row=2,column=2,columnspan=6,ipadx=70,ipady=50,padx=5)
print(unfollowers) # []
if not unfollowers:
    frame3label = tk.Label(frame3, text="No previous follower history", font='Helvetica 10')
    print("hey") #ara mpainei edo
else:
    unf_var = tk.StringVar()
    for i in unfollowers:
        result = i + " "
    unf_var.set(result)
    frame3label = tk.Label(frame3, textvariable=unf_var, font='Helvetica 10')
frame3label.grid()


root.grid_columnconfigure(0, weight=1, uniform="group1")
root.grid_columnconfigure(1, weight=1, uniform="group1")
root.grid_rowconfigure(0, weight=1)

root.mainloop()

