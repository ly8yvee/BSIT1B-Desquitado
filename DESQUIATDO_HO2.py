import tkinter as tk
window = tk.Tk
window.title("DESQUIATDO PROFILE")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg="purple")

profile_label = tk.label(window, text="STUDENT PROFILE", font=("Cooper Black", 14), bg="purple", fg="lightgreen")
full_name_label = tk.label(window, text="Full Name: ROSHLY YVETTE R. DESQUITADO", font=("Cooper Black", 14), bg="purple")
age_label = tk.label(window, text="Age: 19", font=("Cooper Black", 14), bg="purple")
course_section_label = tk.label(window, text="Course and Section: BSIT_18", font=("Cooper Black", 14), bg="purple")
birthday_label = tk.label(window, text="Birthday: OCTOBER 08, 2007", font=("Cooper Black", 14), bg="purple")
motto_label = tk.label(window, text="Personal Motto or Quote: 'Actions speak louder than words' ", font=("Cooper Black", 14), bg="purple")

profile_label.pack(pady=10, anchor="center")
full_name_label.pack(pady=10, anchor="w")
age_label.pack(pady=10, anchor="w")
birthday_label.pack(pady=10, anchor="w")
course_section_label.pack(pady=10, anchor="w")
motto_label.pack(pady=10, anchor="w")

window.mainloop
