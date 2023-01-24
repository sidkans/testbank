import tkinter
from tkinter import *
from tkinter import messagebox
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
        cur.execute("desc information")
    except:
        cur.execute(
            "create table information(id int primary key auto_increment, name varchar(30),age int, gender varchar(6),email varchar(50),pan varchar(10),salary int), password varchar(30)")

    def register():
        cur.execute(
            f"insert into details(name,age,gender,email,pan,salary, password)values('{e2.get()}','{e3.get()}','{e4.get()}','{e5.get()}','{e6.get()}','{e7.get()}, '{e8.get()}')")
        con.commit()
        messagebox.showinfo("Success", "Successfully registered")

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
    l8 = tkinter.Label(win, text="password")

    l1.grid(row=1, column=1, padx=65, pady=10, sticky="nsew")
    l2.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")
    l3.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")
    l4.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")
    l5.grid(row=5, column=1, padx=10, pady=5, sticky="nsew")
    l6.grid(row=6, column=1, padx=10, pady=5, sticky="nsew")
    l7.grid(row=7, column=1, padx=10, pady=5, sticky="nsew")
    l7.grid(row=8, column=1, padx=10, pady=5, sticky="nsew")

    e2 = tkinter.Entry(win)
    e3 = tkinter.Entry(win)
    e4 = tkinter.Entry(win)
    e5 = tkinter.Entry(win)
    e6 = tkinter.Entry(win)
    e7 = tkinter.Entry(win)
    e8 = tkinter.Entry(win)


    e2.grid(row=2, column=2, padx=10, pady=5, sticky="nsew")
    e3.grid(row=3, column=2, padx=10, pady=5, sticky="nsew")
    e4.grid(row=4, column=2, padx=10, pady=5, sticky="nsew")
    e5.grid(row=5, column=2, padx=10, pady=5, sticky="nsew")
    e6.grid(row=6, column=2, padx=10, pady=5, sticky="nsew")
    e7.grid(row=7, column=2, padx=10, pady=5, sticky="nsew")
    e8.grid(row=8, column=2, padx=10, pady=5, sticky="nsew")
    def closebtn():
        win.destroy()
    w = Button(win, text="back to welcome page", command=closebtn).grid(row=9, column=1, padx=50, pady=5, sticky="ns")
    z = Button(win, text="register", command=lambda : [register(), closebtn()]).grid(row=9, column=2, padx=50, pady=5, sticky="ns")


'''
def login():
    con = pymysql.connect(host="localhost", user="root", password="tomriddle@31")
    cur = con.cursor()
    bank_acc_num = firstNameEntry.get()
    password = passwordEntry.get()

    with con.cursor() as cursor:
        sql = "SELECT b FROM details WHERE username=%s AND password=%s"
        cursor.execute(sql, (bank_acc_num, password))
        result = cursor.fetchone()
    if result:
        messagebox.showinfo("Info","Successfully logged in")
    else:
        messagebox.showerror("Error", "Incorrect username or password")
'''''

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

LoginButton = Button(window, text="Login", command=login).pack(pady=5)
forgotpassButton = Button(window, text="ForgotPassword").pack(pady=5)

a=Button(window, text="signup", command=signup).pack(pady=5)
window.mainloop()