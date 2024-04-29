from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import mysql.connector
import os

#connection
my_password = "Plagrange21"
db = "bank_schema"
connection = mysql.connector.connect(
  database = db,
  user="root",
  password= my_password
)
cursor = connection.cursor()
root = Tk()
root.geometry('600x750')
root.eval("tk::PlaceWindow .")

#title 
root.title('Online Banking System')


#frame 


frame = Frame(root,width=500,height=750,bg="white")
frame.place(x=0,y=0)

#image (bg)
LogoImage = PhotoImage(file='/Users/parisdmonkey/Downloads/money-clipart-big-money-clipart-1600.png')
logoLabel = Label(frame,image=LogoImage)
logoLabel.grid(row=1,column=1)

#A label to welcome users at the start 
start = Label(root, text = "Welcome to Online Banking!",padx=240,pady=80,fg="white",bg='green')
start.grid(row=7,column=1)





#this function lets the user view their account balance; tells them how much money they have in their account 
def veiwBalance():
  #this establishes a connection to my sql database 
  connection = mysql.connector.connect(
  database = db,
  user="root",
  password= my_password
  )
  cursor = connection.cursor()
  sql= ("SELECT supplier_balance FROM user_bank_account WHERE supplier_userName = %s")
  
  givenUsername = username_entry.get()
  value = (givenUsername,)
  cursor.execute(sql,value)
  result = cursor.fetchone()
  for r in result:
    message2 = messagebox.showerror("","your balance is "+ str(r) +" dollars")
  
  
  connection.close()
  
  #add money
#this function is supposed to get the users info for the add function
def deposit_money():
  
  deposited_money.grid(row = 12,column= 1)
  entryDeposit.grid(row = 13,column = 1)
  enter_button2.grid(row=13,column = 2)
  
#this functiojn removes user account  
def remove_user_account():
  #this establishes a connection to my sql database 
  connection = mysql.connector.connect(
  database = db,
  user="root",
  password= my_password
  )
  
  cursor = connection.cursor()
  
  #this deletes user based on their username and password they entered 
  sql = ("DELETE FROM user_bank_account WHERE supplier_userName = %s")
  
  givenUsername = username_entry.get()
  
  value = (givenUsername,) # made value into a tuple because i got an error and it said it had to be a tuple 
  
  # this makes sure the user wishes to delete their account and have a second chance
  message1 = messagebox.askyesno("Question","Are you sure you want to delete your account??")

  cursor.execute(sql,value) # this execute the sql to the database 
  result = cursor.fetchall()
  
  if message1: #this basically says if message1 true then#the account is allowed to delete and sends this message for the user to know 
      message2 = messagebox.showerror("","acccount has been deleted")
    
    

      
  
  connection.commit()#this makes the chnage permanent 
  connection.close()

#this is the menu which shows the user options 
#for example viewing account balance, deleting account and adding money 
def menu():
 
  
  bgImage = PhotoImage(file='/Users/parisdmonkey/Downloads/1000_F_305876177_4EzB8UJafxNruTRjfLgc57mb07Qn1cNv.png')
  bgLabel = Label(root,image=bgImage)
  bgLabel.grid(row=1,column=1)
  start = Label(root, text = "Welcome!, What can I help you with! ",padx=200,pady=100,fg="white",bg='green')
  start.grid(row=7,column=1) 
  b_accbalance = Button(root,text="View your account balance",padx=35,command = veiwBalance)
  b_addmoney = Button(root,text="Deposit money",padx=35,command = deposit_money)
  b_deleteacc = Button(root,text="Delete your account",padx=35,command = remove_user_account)
  #money image 

  b_accbalance.place(x=33,y=270) #prints 
  b_addmoney.place(x=40,y=340)#prints
  b_deleteacc.place(x=60,y=400)#prints

#check login basically checks whether the username or password is right/ in database 
#if the password and username is correct it'll continue 
def check_login():
  #establishes an connection to my database
  username = username_entry.get()
  password = pw_entry.get()
  connection = mysql.connector.connect(
  database = db,
  user="root",
  password= my_password
  )
  cursor = connection.cursor()
  
  #selects eveyrthing from table user_banl_account where username and pw are %s (aka the value)
  sql= ("SELECT * FROM user_bank_account WHERE supplier_userName LIKE %s AND supplier_pw LIKE %s")
  
  value = (username,password) #are used for values %s 
  
  cursor.execute(sql,value) 
  
  result = cursor.fetchone()
  
  connection.close()
  if result: #checks if its in the system and if it is then it'll go to the menu 
    menu()
  else: #else show an error and give them another try 
    message = messagebox.showerror("Error","Incorrect Username or Password")

#the labels and buttons for the createacc function
create_pw = Label(root,text="Create a password: ")
create_pwEntry = Entry(root)
create_userNameEntry = Entry(root)
create_userName = Label(root,text="Create a username: ")


def createacc():
  #destroys login page and shows the create account page
  l_username.after(0, l_username.destroy())
  l_password.after(0, l_password.destroy())
  enter_button.after(0, enter_button.destroy())
  pw_entry.after(0, pw_entry.destroy())
  username_entry.after(0, username_entry.destroy())
  option.after(0, option.destroy())
  l_createacc.after(0, l_createacc.destroy())
  
  createButton = Button(root,text='create',command = insert)
  
  
  create_userName.grid(row= 10,column=1)
  create_userNameEntry.grid(row=11,column=1)
  
  create_pw.grid(row=12,column=1)
  create_pwEntry.grid(row=13,column=1)
  
  createButton.grid(row=14,column=1)
  
#this function insert is used in aiding the create acc fucntion
#by inserting users desired information and creating an account 
def insert():
    back_button = Button(root, text = "back")
    created_username = create_userNameEntry.get()
    created_password = create_pwEntry.get()
    start_balance = 0
    connection = mysql.connector.connect(
    database = db,
    user="root",
    password= my_password
    )
    cursor = connection.cursor()
    
    back_button.place(x=500,y=250)
    answer = messagebox.askyesno("Question","Are you sure this is the password and username you want ?")
    sql= ("INSERT INTO user_bank_account(supplier_userName, supplier_pw,supplier_balance) VALUES (%s,%s,%s)")
    value = (created_username,created_password,start_balance)
    
    cursor.execute(sql,value)
    if answer:
      message = messagebox.showerror("","Password has been added, go back to home screen")

    connection.commit()
    connection.close()

#function updates user account and adds whatever amount of money they want to disposit
def add():
  money = entryDeposit.get()
  entered_userName = username_entry.get()
  
  #establishes connection to my database 
  connection = mysql.connector.connect(
  database = db,
  user="root",
  password= my_password
  )
  cursor = connection.cursor()
    
  sql= ("""UPDATE user_bank_account SET supplier_balance = supplier_balance + %s 
          WHERE supplier_userName = %s""")
    
  value = (money,entered_userName)
    
  cursor.execute(sql,value)
  result = cursor.fetchone()
    
  if result:#supposed to show this message after the action is completed  
    message = messagebox.showerror("","Money has been deposited ")
  
#the labels and buttons for the add function
enter_button2 = Button(root, text = 'enter',command = add)
deposited_money = Label(root, text = "How much money do you wish to deposit? ")
entryDeposit = Entry(root)

#buttons and labels for function login_page
l_username = Label(root,text = "Enter your username: ")
l_password = Label(root,text = "Enter your password: ")
option = Label(root,text="If you do not have an account, please create one using button above")

enter_button = Button(root,text= 'Enter',command=check_login)
l_createacc =  Button(root,text = "Create an account",command=createacc)

pw_entry = Entry(root)
username_entry = Entry(root)

supplier_username = username_entry.get()
supplier_password = pw_entry.get()

def login_page(): #login page 
  l_username.grid(row=13,column=1)
  username_entry.grid(row=14,column=1)

  l_password.grid(row=15,column=1)
  pw_entry.grid(row=16,column=1)
  
  enter_button.grid(row=17,column=1)
  l_createacc.grid(row=18,column=1)
  option.grid(row=19,column=1)

login_page()







root.mainloop()



