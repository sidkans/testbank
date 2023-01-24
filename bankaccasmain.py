import tkinter
from tkinter import *

import pymysql
from PIL import ImageTk, Image
window = Tk()
window.title("test bank")

def signup(): #function to link signup toplevel window
    win = tkinter.Toplevel(window)
    con = pymysql.connect(host="localhost", user="root", password="tomriddle@31")
    cur = con.cursor()

    try:
        cur.execute("use bank")
    except:
        cur.execute("create database bank")
        cur.execute("use bank")
    try:
        cur.execute("desc details")
    except:
        cur.execute(
            "create table details(id int primary key auto_increment, name varchar(30),age int, gender varchar(6),email varchar(50),pan varchar(10),salary int)")

    def register():
        cur.execute(
            f"insert into details(name,age,gender,email,pan,salary)values('{e2.get()}','{e3.get()}','{e4.get()}','{e5.get()}','{e6.get()}','{e7.get()}')")
        con.commit()
    image_test = Image.open('backgroundimg.jpg')
    image_0 = image_test.resize((800, 600))
    global bck
    bck = ImageTk.PhotoImage(image_0)
    win.geometry('400x300')
    bgimg = tkinter.Label(win, image=bck)
    bgimg.place(x=0, y=0)
    win.title("signup")

    l1 = tkinter.Label(win, text="personal details")
    l2 = tkinter.Label(win, text="name")
    l3 = tkinter.Label(win, text="age")
    l4 = tkinter.Label(win, text="gender")
    l5 = tkinter.Label(win, text="email")
    l6 = tkinter.Label(win, text="pan card number")
    l7 = tkinter.Label(win, text="salary")

    l1.grid(row=1, column=1, padx=65, pady=10, sticky="nsew")
    l2.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")
    l3.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")
    l4.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")
    l5.grid(row=5, column=1, padx=10, pady=5, sticky="nsew")
    l6.grid(row=6, column=1, padx=10, pady=5, sticky="nsew")
    l7.grid(row=7, column=1, padx=10, pady=5, sticky="nsew")

    e2 = tkinter.Entry(win)
    e3 = tkinter.Entry(win)
    e4 = tkinter.Entry(win)
    e5 = tkinter.Entry(win)
    e6 = tkinter.Entry(win)
    e7 = tkinter.Entry(win)

    e2.grid(row=2, column=2, padx=10, pady=5, sticky="nsew")
    e3.grid(row=3, column=2, padx=10, pady=5, sticky="nsew")
    e4.grid(row=4, column=2, padx=10, pady=5, sticky="nsew")
    e5.grid(row=5, column=2, padx=10, pady=5, sticky="nsew")
    e6.grid(row=6, column=2, padx=10, pady=5, sticky="nsew")
    e7.grid(row=7, column=2, padx=10, pady=5, sticky="nsew")
    def closebtn():
        win.destroy()

    j = Button(win, text="click me", command=lambda : [NewWindow(), closebtn()]).grid(row=8, column=2, padx=50, pady=5, sticky="nsew")
    w = Button(win, text="welcome page", command=closebtn).grid(row=8, column=1, padx=50, pady=5, sticky="ns")


def NewWindow(): #function for ______ toplevel window
    # Toplevel object which will
    # be treated as a new window
    newWindow = tkinter.Toplevel(window)
    image_test = Image.open('backgroundimg.jpg')
    image_0 = image_test.resize((800, 600))
    global bck
    bck = ImageTk.PhotoImage(image_0)
    newWindow.geometry('400x300')
    bgimg = tkinter.Label(newWindow, image=bck)
    bgimg.place(x=0, y=0)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="This is a new window").pack(pady=5)
    def closebtn():
        newWindow.destroy()

    c = tkinter.Button(newWindow, text="sign up", command=lambda : [signup(), closebtn()]).pack(pady=5)
    f = tkinter.Button(newWindow, text="welcome page", command=closebtn).pack(pady=5)


image_test = Image.open('backgroundimg.jpg')
image_0 = image_test.resize((800, 600))
bck_end = ImageTk.PhotoImage(image_0)
window.geometry('400x300')
bgimg = Label(window, image=bck_end)
bgimg.place(x=0, y=0)

titleLabel = Label(window, text="Welcome to test Bank", font=("Lucida", 28)).pack(pady=5)


firstNamelabel = Label(window, text="Enter your bank account number: ").pack(pady=1)
firstNameEntry = Entry(window).pack(pady=5)

passwordlabel = Label(window, text="Enter your password: ").pack(pady=1)
passwordEntry = Entry(window).pack(pady=5)

LoginButton = Button(window, text="Login").pack(pady=5)
forgotpassButton = Button(window, text="ForgotPassword").pack(pady=5)

a=Button(window, text="signup", command=signup).pack(pady=5)
b=Button(window, text="click me", command=NewWindow).pack(pady=5)

window.mainloop()