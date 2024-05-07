from tkinter import *
w = Tk()
w.geometry("1000x500")
img = PhotoImage(file="img.png")
l = Label(image=img)
l.pack()
w.mainloop()