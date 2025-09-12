from tkinter.messagebox import showinfo

import creation_sums
import tkinter
from tkinter import ttk

correct_answer = ""

def enter_values():
    label_output_sums.config(text="")
    lower_border = int(entry_low_border.get())
    higher_border = int(entry_high_border.get())
    num_of_slags = int(entry_number_of_slag.get())
    value = creation_sums.output(lower_border, higher_border, num_of_slags)
    label_output_sums.config(text= value)
    label_output_sums.grid(row=3, column=0, columnspan=3)
    global correct_answer
    correct_answer = eval(value)

def check_answer():
    global correct_answer
    if correct_answer == int(entry_answer.get()):
        showinfo(title="Info", message="Correct answer!")
    else:
        showinfo(title="Info", message="Incorrect answer!")

root = tkinter.Tk()
root.title("mathapp")
root.geometry("590x220")

label_output_sums = ttk.Label(text="Sums here", font=("Times New Roman", 20), wraplength=550)

label_low_border = ttk.Label(text="Low border")
label_low_border.grid(row=0, column=0)

label_number_of_slag = ttk.Label(text="Enter how much num needs")
label_number_of_slag.grid(row=0, column=1)

label_high_border = ttk.Label(text="High border")
label_high_border.grid(row=0, column=2)

entry_low_border = ttk.Entry()
entry_low_border.grid(row=1, column=0)

entry_number_of_slag = ttk.Entry()
entry_number_of_slag.grid(row=1, column=1)

entry_high_border = ttk.Entry()
entry_high_border.grid(row=1, column=2)

where_write_answers_label = ttk.Label(text="Write answer here")
where_write_answers_label.grid(row=5, column=1)

entry_answer = ttk.Entry()
entry_answer.grid(row=6, column=0, columnspan=3)

button_check_answers = ttk.Button(text="Check answer", command=check_answer)
button_check_answers.grid(row=7, column=0, columnspan=3)

button_create_sums = ttk.Button(text= "Create sums", command=enter_values)
button_create_sums.grid(row=2, column=1)

root.mainloop()