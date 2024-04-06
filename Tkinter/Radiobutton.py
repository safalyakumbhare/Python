from tkinter import *
import tkinter.messagebox as box

w = Tk()
w.title("List Box")
w.geometry("400x400")
f = Frame(w)
v1= str()
l = Label(f, text="Select your Course")
l.pack(padx=5, pady=5)
c1 = Radiobutton(f, text="Programming in C",variable=v1,value="Programming in c")
c1.pack(padx=5, pady=5)
c2 = Radiobutton(f, text="Python",variable=v1,value="Python")
c2.pack(padx=5, pady=5)
c3 = Radiobutton(f, text="Java",variable=v1,value="Java")
c3.pack()
c4 = Radiobutton(f, text="VB",variable=v1,value="VB")
c4.pack(padx=5, pady=5)

def mycourse():
    box.showinfo("Checkbox","You Selected : "+v1.get())
b=Button(f,text= "Show Selection", command=mycourse)
b.pack(pady=5)
f.pack()
w.mainloop()
