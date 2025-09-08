import tkinter
from tkinter import ttk

def enter_values():
    lower_border = int(entry_low_border.get())
    high_border = int(entry_high_border.get())
    return lower_border, high_border

root = tkinter.Tk()
root.title("mathapp")
root.geometry("640x480")

label_low_border = ttk.Label(text="Low border")
label_low_border.grid(row=0, column=0)

label_high_border = ttk.Label(text="High border")
label_high_border.grid(row=0, column=2)

entry_low_border = ttk.Entry()
entry_low_border.grid(row=1, column=0)

button_enter_values = ttk.Button(text= "enter border values", command=enter_values)
button_enter_values.grid(row=1, column=1)

entry_high_border = ttk.Entry()
entry_high_border.grid(row=1, column=2)

root.mainloop()