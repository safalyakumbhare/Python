from tkinter import *

w = Tk()
w.title("Radio Button")
w.geometry("300x300")

r1 = Checkbutton(text="Safalya")
r2 = Checkbutton(text="Prajakta")

r1.pack()
r2.pack()

w.mainloop()
