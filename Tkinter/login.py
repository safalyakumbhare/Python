from tkinter import *
import tkinter.messagebox as box
w = Tk()
w.title("Login")
w.geometry("400x400")
def check():
    if e2.get() == "123":
        box.showinfo('Success', 'Correct Password')
    else:
        box.showerror('Error', 'Incorrect Password')
l1 = Label(text="Username")
e1 = Entry()
l2 = Label(text="Password")
e2 = Entry()  
b1 = Button(text="Login", command=check)
l1.pack()
e1.pack()
l2.pack()
e2.pack()
b1.pack()
w.mainloop()