from tkinter import *

import pymysql
from PIL import ImageTk, Image
window = Tk()
window.title("test bank")


image_test = Image.open('backgroundimg.jpg')
image_0 = image_test.resize((800, 600))
bck_end = ImageTk.PhotoImage(image_0)
window.geometry('400x300')
bgimg = Label(window, image=bck_end)
bgimg.place(x=0, y=0)

titleLabel = Label(window, text="Welcome to test Bank", font=("Lucida", 28)).pack(pady=5)