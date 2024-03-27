from tkinter import *
import tkinter.messagebox as box

w = Tk()
w.title("List Box")
w.geometry("400x400")
f = Frame(w)

l = Label(f, text="Select your Course")
l.pack(padx=5, pady=5)
c1 = Checkbutton(f, text="Programming in C", onvalue=1, offvalue=0)
c1.pack(padx=5, pady=5)
c2 = Checkbutton(f, text="Python", onvalue=1, offvalue=0)
c2.pack(padx=5, pady=5)
c3 = Checkbutton(f, text="Java", onvalue=1, offvalue=0)
c3.pack(padx=5, pady=5)
c4 = Checkbutton(f, text="VB", onvalue=1, offvalue=0)
c4.pack(padx=5, pady=5)
c1= IntVar()
c2= IntVar()
c3= IntVar()
c4= IntVar()
def mycourse():
    s=StringVar()
    if c1.get()==1:s+="Programming in C\n"
    if c2.get()==1:s+="Python\n"
    if c3.get()==1:s+="Java\n"
    if c4.get()==1:s+="VB"
    box.showinfo("Checkbox","You Selected : "+s)
b=Button(f,text= "Show Selection", command=mycourse)
b.pack(pady=5)
f.pack()
w.mainloop()
