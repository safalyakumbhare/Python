from tkinter import *
import tkinter.messagebox as box
w = Tk()
w.title("Greeting Form")
w.geometry('400x300')

def hello():
    n=e.get()
    box.showinfo("Greeting","Hello "+n)
    

f = Frame(w)
l = Label(f,text="Enter Your Name ",)
b = Button(f,text="Click",command=hello)
e=Entry(f)
l.pack()
e.pack()
b.pack()

f.pack()
w.mainloop()





