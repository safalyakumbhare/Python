from tkinter import *
w = Tk()
w.title("Entry Control")
w.geometry("400x400")
f = Frame(w)
l = Label(f,text="Enter Your Name")
e = Entry(f)
l.pack()
e.pack()
f.pack()
w.mainloop()