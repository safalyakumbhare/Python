from tkinter import *
import tkinter.messagebox as box
w = Tk()
w.title("Click Event")
w.geometry("400x400")
def click():
    box.showinfo("Msgbox","Button Clicked")
b = Button(text="Click Me",command=click)
b.pack()
w.mainloop()