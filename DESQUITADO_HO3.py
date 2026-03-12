import tkinter as tk

window = tk.Tk()
window.title("simple calculator")
window.geometry("300x220")

result = tk.Label(window, text="")
result.grid(column=0, row=0, columnspan=4)

u_label = tk.Label (window, text="enter 1st number:")
u_label.grid(column=0,row=1,columnspan=2)

u_entry = tk.Entry(window)
u_entry.grid(column=2,row=1,columnspan=2)

p_label = tk.Label (window, text="enter 2nd number:")
p_label.grid(column=0,row=2,columnspan=2)

p_entry = tk.Entry(window)
p_entry.grid(column=2,row=2,columnspan=2)

button = tk.Button(window, text="add")
button.grid(column=2,row=5,columnspan=2)

button = tk.Button(window, text="subract")
button.grid(column=2,row=3,columnspan=2)

button = tk.Button(window, text="multiply")
button.grid(column=0,row=5,columnspan=2)

button = tk.Button(window, text="division")
button.grid(column=0,row=3,columnspan=2)

def add():
    num1 = float(u_entry.get())
    num2 = float(p_entry.get())
    total = num1 + num2
    result.config(text=f"the division of {num1} + {num2} is {total}")

def subtract():
    num1 = float(u_entry.get())
    num2 = float(p_entry.get())
    total = num1 - num2
    result.config(text=f"the division of {num1} - {num2} is {total}")

def multiply():
    num1 = float(u_entry.get())
    num2 = float(p_entry.get())
    total = num1 * num2
    result.config(text=f"the multiply of {num1} * {num2} is {total}")

def division():
    num1 = float(u_entry.get())
    num2 = float(p_entry.get())
    total = num1 / num2
    result.config(text=f"the division of {num1} / {num2} is {total}")

button = tk.Button(window,text="add",command=add)
button.grid(column=2, row=5, columnspan=2)

button = tk.Button(window,text="subtract",command=subtract)
button.grid(column=2, row=3, columnspan=2)

button = tk.Button(window,text="multiply",command=multiply)
button.grid(column=0, row=5, columnspan=2)

button = tk.Button(window,text="division",command=division)
button.grid(column=0, row=3, columnspan=2)

window.mainloop()
