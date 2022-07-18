from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
selection = {}

try:
    continuation_csv = pandas.read_csv("words_to_learn.csv")

except FileNotFoundError:
    csv = pandas.read_csv("french_words.csv")
    data = csv.to_dict(orient="records")
    words_to_learn = csv.to_dict(orient="records")

else:
    words_to_learn = continuation_csv.to_dict(orient="records")


def select_new():
    global selection
    selection = choice(words_to_learn)


def next_card():
    select_new()
    canvas.itemconfigure(background, image=image1)
    canvas.itemconfigure(french, text=f"{selection['French']}")
    canvas.itemconfigure(english, text="")
    window.after(3000, next_card_extension)


def next_card_extension():
    canvas.itemconfigure(english, text=f"{selection['English']}")
    canvas.itemconfigure(background, image=image2)


def right():
    left.config(text=f"{len(words_to_learn)-1}")
    if len(words_to_learn) - 1 != 0:
        words_to_learn.remove(selection)
        data = pandas.DataFrame(words_to_learn)
        data.to_csv("words_to_learn.csv", index=False)
        next_card()


window = Tk()
window.title("FlashCards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

image1 = PhotoImage(file="images/card_front.png")
image2 = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0)
background = canvas.create_image(400, 263, image=image1)
french = canvas.create_text(400, 150, text="", font=("Arial", 48, "bold"))
english = canvas.create_text(400, 263, text="", font=("Arial", 32, "normal"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=3)

image3 = PhotoImage(file="images/wrong.png")
image4 = PhotoImage(file="images/right.png")

wrong_button = Button(image=image3, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

left = Label(text=f"{len(words_to_learn)-1}", font=("Arial", 36, "bold"), bg=BACKGROUND_COLOR)
left.grid(row=1, column=1)

right_button = Button(image=image4, highlightthickness=0, command=right)
right_button.grid(row=1, column=2)

next_card()

window.mainloop()
