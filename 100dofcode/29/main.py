from tkinter import *
from random import choice


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    pw_entry.delete(0, "end")
    char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z",
                 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z",
                 "!", "\'", "^", "-", "+", "%", "&", "/", "(", ")", "=", "?", "_", "<", ">", "£", "#", "$", "{", "[",
                 "]", "}", "@", "~", ".", ":", ";", "|", "\\",
                 "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # https://en.wikipedia.org/wiki/List_of_Special_Characters_for_Passwords

    password = ""
    for password_char in range(int(pw_length_spinbox.get()) + 1):  # "".join(list/tuple) seems interesting
        password += choice(char_list)

    pw_entry.insert(END, password)
    pw_entry.clipboard_append(password)
    status.config(text = f"Password[{pw_length_spinbox.get()}] created and copied to clipboard!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    id = id_entry.get()
    pw = pw_entry.get()
    if id != "" and pw != "" and website != "":
        with open("passwords.csv", mode = "a") as csvfile:
            csvfile.write(f"{website}, {id}, {pw}\n")
        status.config(text = "Saved in passwords.csv!")
    else:
        status.config(text = "Please do not leave any entries empty!")
    website_entry.delete(0, END)
    pw_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
FONTlb = ("Arial", 9, "bold")
FONTes = ("Arial", 8, "normal")

window = Tk()
window.title("Simple CSV Password Manager")
window.config(padx = 10, pady = 10)

status = Label(text = "Welcome to Simple CSV Password Manager", font = FONTlb)  # i hate pop-up boxes so label it is
status.grid(row = 0, column = 0, columnspan = 3)

# image = PhotoImage(file = "logo.png")
# canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
# canvas.create_image(100, 100, image = image)
# canvas.grid(row = 0, column = 1)

website_label = Label(text = "Website:", font = FONTlb)
website_label.grid(row = 1, column = 0)
website_entry = Entry(width = 42, font = FONTes)
website_entry.grid(row = 1, column = 1, columnspan = 2)
website_entry.focus()

id_label = Label(text = "ID:", font = FONTlb)
id_label.grid(row = 2, column = 0)
id_entry = Entry(width = 42, font = FONTes)
id_entry.grid(row = 2, column = 1, columnspan = 2)
id_entry.insert(END, string = "<username>@<mail_provider>.<TLD>")

pw_label = Label(text = "PW:", font = FONTlb)
pw_label.grid(row = 3, column = 0)
pw_entry = Entry(width = 21, font = FONTes)
pw_entry.grid(row = 3, column = 1)
pw_generation_button = Button(text = "Generate Password", command = generate_pw, font = FONTlb)
pw_generation_button.grid(row = 3, column = 2)

add_button = Button(text = "Add", width = 35, command = add, font = FONTlb)
add_button.grid(row = 4, column = 1, columnspan = 2)

pw_length_label = Label(text = "PW Length:", font = FONTlb)
pw_length_label.grid(row = 5, column = 0)
pw_length_spinbox = spinbox = Spinbox(from_ = 8, to = 32, width = 10, font = FONTes)
pw_length_spinbox.grid(row = 5, column = 1)

window.mainloop()
