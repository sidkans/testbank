from tkinter import *
window = Tk()

titleLabel = Label(window,text="Welcome to Humsafar Bank",font=("Lucida",30)).grid(row=0,column=0,columnspan=2)

firstNamelabel = Label(window,text = "Enter your bank account number: ").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

passwordlabel = Label(window,text = "Enter your password: ").grid(row=2,column=0)
passwordEntry = Entry(window).grid(row=2,column=1)

LoginButton = Button(window,text="Login").grid(row=3,column=0,columnspan=2)
forgotpassButton = Button(window, text="ForgotPassword").grid(row=4, column=0, columnspan=2)

window.mainloop()