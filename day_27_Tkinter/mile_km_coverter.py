from tkinter import *

window = Tk()

window.title("Miles to Km converter")
window.config(padx=20,pady=20)

entry = Entry(width=7)
entry.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

km_label = Label(text="0")
km_label.grid(column=1,row=1)

km_show_label = Label(text="km")
km_show_label.grid(column=2,row=1)
def convert():
    var = entry.get()
    var = float(var) * 1.60934
    km_label.config(text=str(var))

button = Button(text="convert", command=convert)
button.grid(column=1,row=2)





window.mainloop()