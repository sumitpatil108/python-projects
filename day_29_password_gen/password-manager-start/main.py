from tkinter import *
from random import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password2 = "".join(password_list)
    password.insert(0, password2)
    pyperclip.copy(password2)


# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox

def search():
    website2 = website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website2 in data:
            email = data[website2]["email/username"]
            password3 = data[website2]["password"]
            messagebox.showinfo(title=website2, message=f"Email: {email}\npassword: {password3}")
        else:
            messagebox.showinfo(title="Error", message=f"No {website2} Exists")



def save():
    website1 = website.get()
    email1 = gmail.get()
    password1 = password.get()
    new_data = {
        website1: {
            "email/username": email1,
            "password": password1,
        }
    }

    if len(website1) == 0 or len(password1) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email1} "
        #                                               f"\nPassword: {password1} \nIs it ok to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # data_file.write(f"{website1} | {email1} | {password1}\n")
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website.delete(0, END)
            gmail.delete(0, END)
            password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Genrator")
window.config(padx=50, pady=50, bg="black")

canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=img)
canvas.grid(column=1, row=0)

# ...............entrypoint......................
website_label = Label(text="website: ", bg="black", fg="white")
website_label.grid(column=0, row=1)

website = Entry(width=30)
#website.insert(END, string="website: ")
website.grid(column=1, row=1)

button_search = Button(text="Search", command=search)
button_search.grid(column=2,row=1)

gmail_label = Label(text="gmail/username: ", bg="black", fg="white")
gmail_label.grid(column=0, row=2)

gmail = Entry(width=41)
#gmail.insert(END, string="gmail/username: ")
gmail.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password: ", bg="black", fg="white")
password_label.grid(column=0, row=3)

password = Entry(width=30)
password.grid(column=1, row=3)

genrate_button = Button(text="Genrate", command=generate_password)
genrate_button.grid(column=2, row=3)

save_button = Button(text="Save", width=38, command=save)
save_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
