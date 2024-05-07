from tkinter import *
w = Tk()
w.title("List Box")
w.geometry("400x400")
l = Listbox()
l.insert(0,"Mouse")
l.insert(1,"Keyboard")
l.insert(2,"Laptop")
l.insert(3,"Headphones")
l.insert(4,"Speakers")

l.pack()
w.mainloop()