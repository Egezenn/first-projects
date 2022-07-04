from tkinter import *
from random import choice
import json


def generate_pw():
    pw_entry.delete(0, END)
    char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z",
                 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z",
                 "!", "\'", "^", "-", "+", "%", "&", "/", "(", ")", "=", "?", "_", "<", ">", "£", "#", "$", "{", "[",
                 "]", "}", "@", "~", ".", ":", ";", "|", "\\", " ", ",",
                 "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # https://en.wikipedia.org/wiki/List_of_Special_Characters_for_Passwords

    password = ""
    for password_char in range(int(pw_length_spinbox.get()) + 1):  # "".join(list/tuple) seems interesting
        password += choice(char_list)

    pw_entry.insert(END, password)
    pw_entry.clipboard_append(password)
    status.config(text=f"Password[{pw_length_spinbox.get()}] created and copied to clipboard!")


def add():
    website = website_entry.get()
    id = id_entry.get()
    pw = pw_entry.get()

    new_login = {
        website: {
            "id": id,
            "pw": pw
        }
    }

    if id != "" and pw != "" and website != "":
        try:
            with open("passwords.json", mode="r") as json_file:
                data = json.load(json_file)
                data.update(new_login)

        except FileNotFoundError:
            with open("passwords.json", mode="w") as json_file:
                json.dump(new_login, json_file, indent=4)
            status.config(text="Saved in passwords.json!")

        else:
            with open("passwords.json", mode="w") as json_file:
                json.dump(data, json_file, indent=4)

        finally:
            status.config(text="Saved in passwords.json!")
            website_entry.delete(0, END)
            pw_entry.delete(0, END)

    else:
        status.config(text="Please do not leave any entries empty!")


def search():

    with open("passwords.json") as json_file:
        website = website_entry.get()
        data = json.load(json_file)

        if website in data:
            id = data[website]["id"]
            pw = data[website]["pw"]
            id_entry.delete(0, END)
            pw_entry.delete(0, END)
            id_entry.insert(END, id)
            pw_entry.insert(END, pw)

        else:
            status.config(text="Key not found!")


window = Tk()
window.title("Simple JSON Password Manager")
window.config(padx=10, pady=10)

status = Label(text="Welcome to Simple JSON Password Manager")  # i hate pop-up boxes so label it is
status.grid(row=0, column=0, columnspan=3)

# image = PhotoImage(file = "logo.png")
# canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
# canvas.create_image(100, 100, image = image)
# canvas.grid(row = 0, column = 1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_search_button = Button(text="Search", width=16, command=search)
website_search_button.grid(row=1, column=2)
website_entry.focus()

id_label = Label(text="ID:")
id_label.grid(row=2, column=0)
id_entry = Entry(width=40)
id_entry.grid(row=2, column=1, columnspan=2)
id_entry.insert(END, string="<username>@<mail_provider>.<TLD>")

pw_label = Label(text="PW:")
pw_label.grid(row=3, column=0)
pw_entry = Entry(width=21)
pw_entry.grid(row=3, column=1)
pw_generation_button = Button(text="Generate Password", command=generate_pw)
pw_generation_button.grid(row=3, column=2)

add_button = Button(text="Add", width=38, command=add)
add_button.grid(row=4, column=1, columnspan=2)

pw_length_label = Label(text="PW Length:")
pw_length_label.grid(row=5, column=0)
pw_length_spinbox = spinbox = Spinbox(from_=8, to=32, width=10)
pw_length_spinbox.grid(row=5, column=1)

window.mainloop()
