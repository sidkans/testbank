from tkinter import *
from PIL import ImageTk, Image

window = Tk()

window.title("test bank")

image_test = Image.open('download.jpg')
image_0 = image_test.resize((800, 600))
bck_end = ImageTk.PhotoImage(image_0)
window.geometry('800x600')
'''
bgimg = Label(window, image=bck_end)
bgimg.place(x=0, y=0)
'''
titleLabel = Label(window, text="Welcome to test Bank")
titleLabel.grid(row = 1, column = 1)

firstNamelabel = Label(window, text="Enter your bank account number: ")
firstNamelabel.grid(row = 2, column = 1)
firstNameEntry = Entry(window)
firstNameEntry.grid(row = 2, column = 2)

passwordlabel = Label(window, text="Enter your password: ")
passwordlabel.grid(row = 3, column = 1)
passwordEntry = Entry(window)
passwordEntry.grid(row = 3, column = 2)

LoginButton = Button(window, text="Login")
LoginButton.grid(row = 4, column = 1)
forgotpassButton = Button(window, text="ForgotPassword")
forgotpassButton.grid(row = 5, column = 1)

window.mainloop()