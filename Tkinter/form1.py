from tkinter import *
import tkinter.messagebox as box
w = Tk()
w.geometry("400x300")
def hello():
    box.showinfo("Information","Python GUI")
    
    
w.title("Student Admission Form")
Button(text="Click",command=hello).pack(padx=10)

