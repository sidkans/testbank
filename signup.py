import tkinter
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
win.geometry("500x500")
win.title("signup")
l1 = tkinter.Label(win,text="personal details" )
l2 = tkinter.Label(win,text="name" )
l3 = tkinter.Label(win,text="age" )
l4 = tkinter.Label(win,text="gender")
l5 = tkinter.Label(win,text="email")
l6 = tkinter.Label(win,text="pan card number")
l7 = tkinter.Label(win,text="salary")
l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
l3.grid(row=3,column=1)
l4.grid(row=4,column=1)
l5.grid(row=5,column=1)
l6.grid(row=6,column=1)
l7.grid(row=7,column=1)

e2 = tkinter.Entry(win)
e3 = tkinter.Entry(win)
e4 = tkinter.Entry(win)
e5 = tkinter.Entry(win)
e6 = tkinter.Entry(win)
e7 = tkinter.Entry(win)

e2.grid(row=2, column=2)
e3.grid(row=3, column=2)
e4.grid(row=4, column=2)
e5.grid(row=5, column=2)
e6.grid(row=6, column=2)
e7.grid(row=7, column=2)

b = tkinter.Button(win, text="submit", command=register)
b.grid(row=8, column=1)

win.mainloop()