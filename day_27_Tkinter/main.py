from tkinter import *

window = Tk()

window.title("my first Gui project")
window.minsize(width=600, height=300)

def button_clicked():
    new_text = input.get()
    label = Label(text=new_text)
    label.pack()



button = Button(text="click me",command=button_clicked)
button.pack()


input = Entry(width=10)
input.pack()

window.mainloop()