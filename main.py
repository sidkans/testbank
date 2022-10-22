from tkinter import *
from PIL import ImageTk, Image
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