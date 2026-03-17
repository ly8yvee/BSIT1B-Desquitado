import tkinter as tk
from datetime import datetime

window = tk.Tk()
window.title("Profile Builder")
window.geometry("500x250")
window.config(bg="purple")

first_name = tk.StringVar()
middle_name = tk.StringVar()
last_name = tk.StringVar()
birth_year = tk.StringVar()
age_text = tk.StringVar()
gender = tk.StringVar()

def compute_age(event):
    year = int(birth_year.get())
    current_year = datetime.now().year
    age = current_year - year
    age_text.set("Age: " + str(age))

def change_color():
    if gender.get() == "Male":
        window.config(bg="lightblue")
    elif gender.get() == "Female":
        window.config(bg="pink")

def hover_enter(e):
    submit_btn.config(bg="yellow")

def hover_leave(e):
    submit_btn.config(bg="white")

def generate_id():
    id_window = tk.Toplevel()
    id_window.title("Student ID Card")
    id_window.geometry("300x200")

    name = first_name.get() + " " + middle_name.get() + " " + last_name.get()

    tk.Label(id_window, text="STUDENT ID CARD", font=("Arial",14,"bold")).pack(pady=10)
    tk.Label(id_window, text="Name: " + name).pack()
    tk.Label(id_window, text="Age: " + age_text.get().replace("Age: ","")).pack()
    tk.Label(id_window, text="Gender: " + gender.get()).pack()

tk.Label(window, text="Profile Builder", font=("Arial",14,"bold"), bg="lightgreen").pack(pady=5)

frame1 = tk.Frame(window, bg="lightgreen")
frame1.pack()

tk.Entry(frame1, textvariable=first_name).grid(row=0,column=0,padx=5)
tk.Entry(frame1, textvariable=middle_name).grid(row=0,column=1,padx=5)
tk.Entry(frame1, textvariable=last_name).grid(row=0,column=2,padx=5)

tk.Label(frame1,text="First Name",bg="lightgreen").grid(row=1,column=0)
tk.Label(frame1,text="Middle Name",bg="lightgreen").grid(row=1,column=1)
tk.Label(frame1,text="Last Name",bg="lightgreen").grid(row=1,column=2)

frame2 = tk.Frame(window, bg="lightgreen")
frame2.pack(pady=5)

birth_entry = tk.Entry(frame2, textvariable=birth_year)
birth_entry.grid(row=0,column=0)
birth_entry.bind("<Return>", compute_age)

tk.Label(frame2,text="Birth Year",bg="lightgreen").grid(row=1,column=0)

tk.Label(window, textvariable=age_text, font=("Arial",12), bg="lightgreen").pack()

frame3 = tk.Frame(window, bg="lightgreen")
frame3.pack()

tk.Label(frame3,text="Gender",bg="lightgreen").grid(row=0,column=0)

tk.Radiobutton(frame3,text="Male",variable=gender,value="Male",
               command=change_color,bg="lightgreen").grid(row=0,column=1)

tk.Radiobutton(frame3,text="Female",variable=gender,value="Female",
               command=change_color,bg="lightgreen").grid(row=0,column=2)

submit_btn = tk.Button(window,text="Submit",command=generate_id,bg="white")
submit_btn.pack(pady=10)

submit_btn.bind("<Enter>", hover_enter)
submit_btn.bind("<Leave>", hover_leave)

window.mainloop()