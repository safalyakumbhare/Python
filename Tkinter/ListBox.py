from tkinter import *
import tkinter.messagebox as box
w=Tk()
w.title("List Box")
w.geometry('400x400')
f = Frame(w)
l=Label(f,text="Select your course")
l.pack(padx=5,pady=5)
f.pack(padx=5,pady=5)

lt = Listbox(f)
lt.pack(padx=5,pady=5)
lt.insert(0,"BCCA")
lt.insert(1,"BBA")
lt.insert(2,"BCA")
lt.insert(3,"MBA")
lt.insert(4,"MCA")

def myc():
    box.showinfo("Listbox",lt.get(lt.curselection()))
b=Button(f,text="Show Your Selection",command=myc)
b.pack()
w.mainloop()