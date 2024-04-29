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
  #sql code that selects the balance in the system based on the username because the username is the primary key
  #because in websites or apps they don't let you have the same password 

  #I tried to use try and except for the error
  #and just make it print the username is already taken but I wasn't able to figure it out 
#I thought that if I just put the error in try and put the message = messagebox... in execept it would work but no it didn't 

  
  givenUsername = username_entry.get() #gets the users username 
  
  value = (givenUsername,)#made this into a tuple because otherwise it won't work 
  
  cursor.execute(sql,value)
  
  result = cursor.fetchone() #fetchs the results from my databse 
  
  for r in result:
    message2 = messagebox.showerror("","your balance is "+ str(r) +" $")
  #for example 
  #if the users account balance is 100 itll print Your balance is 100$
  
  connection.close()
  
  #add money
#this function is supposed to get the users info for the add function
def deposit_money():
  
  #prints the variables 
  #I was trying to seperate it because I did it all in one function but whenever it would never add to my system 
  #and I think its because it would go back to the input/labels without accually executing in my database 
  #but the sql code works just find its just the matter of accomplishing it in tkinter

  
  I told the 'enter' button to go the add 
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
  bgLabel = Label(root,image=bgImage)   #the money image in the background 
  bgLabel.grid(row=1,column=1) #prints the image 
  start = Label(root, text = "Welcome!, What can I help you with! ",padx=200,pady=100,fg="white",bg='green') 
  #this is the big green welcome at the start 
  start.grid(row=7,column=1) 
  
  b_accbalance = Button(root,text="View your account balance",padx=35,command = veiwBalance) #viewBalance
  b_addmoney = Button(root,text="Deposit money",padx=35,command = deposit_money)#deposit_money
  b_deleteacc = Button(root,text="Delete your account",padx=35,command = remove_user_account) #remove account 
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
#out of the function once again because I use them across the code 
create_pw = Label(root,text="Create a password: ")
create_pwEntry = Entry(root)                     #variables for creating username/password 
create_userNameEntry = Entry(root)
create_userName = Label(root,text="Create a username: ")


def createacc():
  #destroys login page and shows the create account page
  l_username.after(0, l_username.destroy())
  l_password.after(0, l_password.destroy())
  enter_button.after(0, enter_button.destroy())
  pw_entry.after(0, pw_entry.destroy())              #alll this code just destroys all the code in the login_page 
  username_entry.after(0, username_entry.destroy())    #create acc label, username label/input etc
  option.after(0, option.destroy())
  l_createacc.after(0, l_createacc.destroy())
  
  createButton = Button(root,text='create',command = insert)#this is the create button and whne this is pressed the users account get created 
  #and added to the database 
  
  
  create_userName.grid(row= 10,column=1) 
  create_userNameEntry.grid(row=11,column=1)            #prints create username label and input
  
  create_pw.grid(row=12,column=1)                       #prints create password label and input 
  create_pwEntry.grid(row=13,column=1)
  
  createButton.grid(row=14,column=1)
  
#this function insert is used in aiding the create acc fucntion
#by inserting users desired information and creating an account 
def insert():
    back_button = Button(root, text = "back") #this was supposed to go back to make it convient for the users
  #but I had problems switching using destroy and then I tried using forget but for some reason the code was still showing up on the screen
  
    created_username = create_userNameEntry.get()#gets the just created username 
    created_password = create_pwEntry.get() #gets the just created password 
    start_balance = 0 #default value 
  #connection to database 
    connection = mysql.connector.connect(
    database = db,
    user="root",
    password= my_password
    )
    cursor = connection.cursor()
    
    back_button.place(x=500,y=250)
    answer = messagebox.askyesno("Question","Are you sure this is the password and username you want ?")
    sql= ("INSERT INTO user_bank_account(supplier_userName, supplier_pw,supplier_balance) VALUES (%s,%s,%s)")
  #sql code to insert users data into my sql database 
    value = (created_username,created_password,start_balance)
    
    cursor.execute(sql,value)
    if answer:#checks whether answer is true or false 
      #if true then this message will pop up 
      message = messagebox.showerror("","Password has been added, go back to home screen")

    connection.commit() #makes chnage permament 
    connection.close()

#function updates user account and adds whatever amount of money they want to disposit
def add():
  money = entryDeposit.get() #gets the users amount they inputted to be deposited 
  entered_userName = username_entry.get()#gets the users username 
  
  #establishes connection to my database 
  connection = mysql.connector.connect(
  database = db,
  user="root",
  password= my_password
  )
  cursor = connection.cursor()

  #code works in sql but didn't have enough time to debug this out and make it bring out
  #biggest problem I had was the enter button for this 
  #and the fact that my labels and stuff were not showing unless i had a new frame which made it hard to use the enter button 
  #because i couldn't make the new frame universal like the labels and inputs at the bottom.
  sql= ("""UPDATE user_bank_account SET supplier_balance = supplier_balance + %s 
          WHERE supplier_userName = %s""") #sql code 
    
  value = (money,entered_userName)#values to use for the code 
    
  cursor.execute(sql,value)
  result = cursor.fetchone()
    
  if result:#supposed to show this message after the action is completed  
    message = messagebox.showerror("","Money has been deposited ")
  
#the labels and buttons for the add function(they're down here because I use them in functions above
#and if I don't put them at the bottom then I won't be able to use them.

enter_button2 = Button(root, text = 'enter',command = add) #this enter button goes to the add def function 
deposited_money = Label(root, text = "How much money do you wish to deposit? ") #this is just an text label 
entryDeposit = Entry(root) #and this is the input of the text label above 

#buttons and labels for function login_page
l_username = Label(root,text = "Enter your username: ")#label
l_password = Label(root,text = "Enter your password: ")#label
option = Label(root,text="If you do not have an account, please create one using button above")#label 

enter_button = Button(root,text= 'Enter',command=check_login) #button used in the start - 
#when you press it, it checks your login to see if you're in the system and have an account

l_createacc =  Button(root,text = "Create an account",command=createacc) #button used in beginning for users who don't have an account with us 

pw_entry = Entry(root) #input for users password
username_entry = Entry(root)#input for users username

supplier_username = username_entry.get() #gets the users username
supplier_password = pw_entry.get()#gets the users password

def login_page(): #login page (prints all the fields leaving the varables out side
  l_username.grid(row=13,column=1) #prints user label
  username_entry.grid(row=14,column=1)#prints username input

  l_password.grid(row=15,column=1)#prints password label
  pw_entry.grid(row=16,column=1) #prints password input
  
  enter_button.grid(row=17,column=1)#prints enter Button
  l_createacc.grid(row=18,column=1) #prints the option create an account
  option.grid(row=19,column=1)#prints the text label to let users know to create an account

login_page()







root.mainloop() #this is what launches the app 



