from tkinter import *
from tkinter import colorchooser as cc



def ask_color():
    b = cc.askcolor()
    print(b)

x = int(input("How Many Chooses : "))

for i in range(x):
    ask_color()
    

