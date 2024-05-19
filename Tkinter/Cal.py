import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=16, borderwidth=4, font=('Arial', 24))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=button_clear).grid(row=row, column=col)
    elif button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=button_equal).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
