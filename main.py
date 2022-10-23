from tkinter import *
from PIL import ImageTk, Image
import pymysql


con = pymysql.connector.connect(host='localhost', user='root', password='humtum', database='hello')
cur = con.cursor(buffered=True)

try:
   cur.execute("SignUp")
except:
    cur.execute("create database registration")
    cur.execute("use SignUp")

try:
    cur.execute("describe persons")
except:
    cur.execute("create table bank(id int primary key auto_increment, name varchar(50), age int, gender varchar(5), email varchar(50), mobile varchar(11))")
    def SignUp():
        cur.execute(f"insert into bank(name, age, gender, email, mobile) values ('{e1.get()},'{e2.get()}',{e3.get()}',{e4.get()},'{e5.get()}')")

window = Tk()

window.title("test bank")

image_test = Image.open('download.jpg')
image_0 = image_test.resize((800, 600))
bck_end = ImageTk.PhotoImage(image_0)
window.geometry('800x600')
bgimg = Label(window, image=bck_end)
bgimg.place(x=0, y=0)

titleLabel = Label(window, text="Welcome to test Bank", font=("Lucida", 28)).pack(pady=5)


firstNamelabel = Label(window, text="Enter your bank account number: ").pack(pady=1)
firstNameEntry = Entry(window).pack(pady=5)

passwordlabel = Label(window, text="Enter your password: ").pack(pady=1)
passwordEntry = Entry(window).pack(pady=5)

LoginButton = Button(window, text="Login").pack(pady=5)
forgotpassButton = Button(window, text="ForgotPassword").pack(pady=5)

window.mainloop()