from tkinter import *

w = Tk()
l = Label(w)


def click():
    l.config(text="Click ho gaya yeee!")


b = Button(w, text="Submit", command=click)
l.pack(padx=12)
b.pack(padx=30)
w.geometry("300x300")
w.mainloop()
