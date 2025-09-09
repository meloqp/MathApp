import creation_sums
import tkinter
from tkinter import ttk

def enter_values():
    lower_border = int(entry_low_border.get())
    higher_border = int(entry_high_border.get())
    num_of_slags = int(entry_number_of_slag.get())
    s = creation_sums.output(lower_border, higher_border, num_of_slags)
    listbox_output.insert(0, s)
    return lower_border, higher_border, num_of_slags

root = tkinter.Tk()
root.title("mathapp")
root.geometry("640x480")

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

button_enter_values = ttk.Button(text= "enter border values", command=enter_values)
button_enter_values.grid(row=2, column=1)

listbox_output = tkinter.Listbox()
listbox_output.grid(row=3, column=1)

root.mainloop()