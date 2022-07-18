# from tkinter import *
#
#
# def button_clicked():
#     uinput = user_input.get()
#     if uinput != "":
#         a_label.config(text = f"{uinput}")
#
#
# window = Tk()
# window.title("Graphical User Interface")
# window.minsize(500, 300)
#
# a_label = Label(text = "Set the title!", font = ("Arial", 24, "bold"))
# a_label.pack()
#
# button = Button(text = "Write the title you desire and click to set the title!", command = button_clicked)
# button.pack()
#
# user_input = Entry()
# user_input.config(width = 10)
# user_input.pack()
#
#
# window.mainloop()

# def add(*args):
#     total = 0
#     for arg in args:
#         print(arg)
#     for n in args:
#         total += n
#     return total
#
#
# print(add(4,5,6,3))

# def calc(**kwargs):
#     print(kwargs["add"])
#
#
# calc(add=3, multiply=5)

# from tkinter import *
#
# window = Tk()
# window.minsize(500, 300)
# window.config(padx=100, pady=200)
#
# label = Label(text = "Label", font=("Arial", 13, "bold"))
# label.grid(row=0, column=0)
#
# button = Button(text = "1111")
# button.grid(row=1, column=1)
#
# another_button = Button(text = "2222")
# another_button.grid(row=0, column=2)
#
# entry = Entry(width=10)
# entry.insert(END, "Entry")
# entry.grid(row=3, column=3)
#
# window.mainloop()
