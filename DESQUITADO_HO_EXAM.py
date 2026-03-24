from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("DESQUITADO HO EXAM")
window.geometry("400x300")

stored_username = ""
stored_password = ""

def open_register():
    reg = Toplevel(window)
    reg.title("Register")
    reg.geometry("350x250")
    reg.config(bg="green")

    def toggle_password():
        if show_var.get():
            password_entry.config(show="")
        else:
            password_entry.config(show="*")

    def register_user():
        global stored_username, stored_password
        username = username_entry.get()
        password = password_entry.get()

        if len(password) < 8:
            message_label.config(text="Password must be at least 8 characters!", bg="red")
        else:
            stored_username = username
            stored_password = password
            message_label.config(text="You have successfully registered!", bg="green")

    message_label = Label(reg, text="", fg="white", bg="green")
    message_label.pack()

    Label(reg, text="Username:", bg="green").pack()
    username_entry = Entry(reg)
    username_entry.pack()

    Label(reg, text="Password:", bg="green").pack()
    password_entry = Entry(reg, show="*")
    password_entry.pack()

    show_var = IntVar()
    Checkbutton(reg, text="See Password", variable=show_var, command=toggle_password, bg="green").pack()

    Button(reg, text="Register", command=register_user).pack(pady=10)

def open_login():
    log = Toplevel(window)
    log.title("Log In")
    log.geometry("350x250")
    log.config(bg="red")

    def toggle_password():
        if show_var.get():
            password_entry.config(show="")
        else:
            password_entry.config(show="*")

    def login_user():
        username = username_entry.get()
        password = password_entry.get()

        if username == stored_username and password == stored_password:
            message_label.config(text="Login Successful!", bg="green")
        else:
            message_label.config(text="Your user credentials are incorrect!", bg="red")

    message_label = Label(log, text="", fg="white", bg="red")
    message_label.pack()

    Label(log, text="Username:", bg="red").pack()
    username_entry = Entry(log)
    username_entry.pack()

    Label(log, text="Password:", bg="red").pack()
    password_entry = Entry(log, show="*")
    password_entry.pack()

    show_var = IntVar()
    Checkbutton(log, text="See Password", variable=show_var, command=toggle_password, bg="red").pack()

    Button(log, text="Log In", command=login_user, bg="green").pack(pady=10)

Label(window, text="Welcome!", font=("Arial", 20)).pack(pady=10)

Button(window, text="Register", bg="blue", fg="black", width=20, height=2, command=open_register).pack(pady=10)
Button(window, text="Log In", bg="green", fg="black", width=20, height=2, command=open_login).pack(pady=10)

window.mainloop()
