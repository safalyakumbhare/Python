from tkinter import *

w = Tk()
w.geometry("644x900")
w.title("Simple Calculator")


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        pass
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


scvalue = StringVar()
scvalue.set("")
screen = Entry(w, textvar=scvalue, font="lucida 40 bold")

screen.pack(fill=X, ipadx=5, pady=10, padx=10)


f = Frame(w, bg="grey")
b = Button(f, text="9", padx=28, pady=22, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=12)
b = Button(f, text="8", padx=28, pady=22, font="lucida 35 bold")

b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text="7", padx=28, pady=22, font="lucida 35 bold")

b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(w, bg="grey")
b = Button(f, text="6", padx=28, pady=22, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=12)
b = Button(f, text="5", padx=28, pady=22, font="lucida 35 bold")

b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text="4", padx=28, pady=22, font="lucida 35 bold")

b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(w, bg="grey")
b = Button(f, text="3", padx=28, pady=22, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=12)
b = Button(f, text="2", padx=28, pady=22, font="lucida 35 bold")

b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text="1", padx=28, pady=22, font="lucida 35 bold")

b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(w, bg="grey")
b = Button(f, text="3", padx=28, pady=22, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=12)
b = Button(f, text="2", padx=28, pady=22, font="lucida 35 bold")

b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text="1", padx=28, pady=22, font="lucida 35 bold")

b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()



w.mainloop()
