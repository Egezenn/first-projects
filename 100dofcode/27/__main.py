from tkinter import *


def miles_to_km():
    global ENTRY, KILOMETERS_DISPLAY
    uinput = int(ENTRY.get())
    kilometers = round(uinput * 1.609, 2)
    ENTRY.delete(0, END)
    ENTRY.insert(END, f"{uinput} miles")
    KILOMETERS_DISPLAY.delete(0, END)
    KILOMETERS_DISPLAY.insert(END, f"{kilometers} kilometers")


FONT = ("Arial", 12, "bold")
FONTa = ("Arial", 12, "italic")

window = Tk()
window.title("miles to km")
window.config(padx = 20, pady = 20)

ENTRY = Entry(width = 10, font = FONTa)
ENTRY.insert(END, "enter miles")
ENTRY.pack(side = "left")

equal_to = Label(text = "==", font = FONT)
equal_to.pack(side = "left", padx = 5)

KILOMETERS_DISPLAY = Entry(width = 15, font = FONTa)
KILOMETERS_DISPLAY.insert(END, "kilometers")
KILOMETERS_DISPLAY.pack(side = "left")

button = Button(text = "calculate", font = FONT, command = miles_to_km)
button.pack(side = "left", padx = 10)

window.mainloop()
