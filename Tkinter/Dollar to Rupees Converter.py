from tkinter import *
import tkinter.messagebox as box
w = Tk()

w.geometry('350x250')   
def con():
    amt = int(t.get())
    rs = amt * 82.89015
    box.showinfo("Dol to Rs","Rs "+ str(rs))
w.title("Dollar to Rs Converter")
l1 = Label(w,text="Welcome to Dollar to Rupees Converter")
l2 = Label(w,text="Enter the Dollars amount: ")
b = Button(w,text="convert", command=con)
t = Entry(w)
l1.pack()
l2.pack()
t.pack()
b.pack()


w.mainloop()