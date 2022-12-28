import tkinter
from PIL import ImageTk, Image
import pymysql

con = pymysql.connect(host="localhost", user="root", password="fashbooster2004!")
cur = con.cursor()

try:
    cur.execute("use bank")
except:
    cur.execute("create database bank")
    cur.execute("use bank")
try:
    cur.execute("desc details")
except:
    cur.execute("create table details(id int primary key auto_increment, name varchar(30),age int, gender varchar(6),email varchar(50),pan varchar(10),salary int)")

def register():
    cur.execute(f"insert into details(name,age,gender,email,pan,salary)values('{e2.get()}','{e3.get()}','{e4.get()}','{e5.get()}','{e6.get()}','{e7.get()}')")
    con.commit()

win = tkinter.Tk()

image_test = Image.open('backgroundimg.jpg')
image_0 = image_test.resize((800, 600))
bck_end = ImageTk.PhotoImage(image_0)
win.geometry('400x300')
bgimg = tkinter.Label(win, image=bck_end)
bgimg.place(x=0, y=0)
win.title("signup")

l1 = tkinter.Label(win,text="personal details" )
l2 = tkinter.Label(win,text="name" )
l3 = tkinter.Label(win,text="age" )
l4 = tkinter.Label(win,text="gender")
l5 = tkinter.Label(win,text="email")
l6 = tkinter.Label(win,text="pan card number")
l7 = tkinter.Label(win,text="salary")

l1.grid(row=1,column=1,padx=65, pady=10, sticky="nsew")
l2.grid(row=2,column=1,padx=10, pady=5, sticky="nsew")
l3.grid(row=3,column=1,padx=10, pady=5, sticky="nsew")
l4.grid(row=4,column=1,padx=10, pady=5, sticky="nsew")
l5.grid(row=5,column=1,padx=10, pady=5, sticky="nsew")
l6.grid(row=6,column=1,padx=10, pady=5, sticky="nsew")
l7.grid(row=7,column=1,padx=10, pady=5, sticky="nsew")

e2 = tkinter.Entry(win)
e3 = tkinter.Entry(win)
e4 = tkinter.Entry(win)
e5 = tkinter.Entry(win)
e6 = tkinter.Entry(win)
e7 = tkinter.Entry(win)

e2.grid(row=2, column=2,padx=10, pady=5, sticky="nsew")
e3.grid(row=3, column=2,padx=10, pady=5, sticky="nsew")
e4.grid(row=4, column=2,padx=10, pady=5, sticky="nsew")
e5.grid(row=5, column=2,padx=10, pady=5, sticky="nsew")
e6.grid(row=6, column=2,padx=10, pady=5, sticky="nsew")
e7.grid(row=7, column=2,padx=10, pady=5, sticky="nsew")

b = tkinter.Button(win, text="submit", command=register)
b.grid(row=8, column=1,padx=100, pady=5, sticky="nsew")

win.mainloop()