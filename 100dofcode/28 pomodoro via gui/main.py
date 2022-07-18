from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#FFFFFF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15


# ---------------------------- BUTTON COMMANDS ------------------------------- #
COUNT = 1


def start():
    global COUNT, LONG_BREAK_MIN, SHORT_BREAK_MIN, text

    timer_count = WORK_MIN * 60
    break_timer_count_short = SHORT_BREAK_MIN * 60
    break_timer_count_long = LONG_BREAK_MIN * 60

    if COUNT % 2 == 1:
        text.config(text = f"{COUNT}. Work")  # TODO fix this
        count_down(timer_count)

    elif COUNT % 2 == 0:  # my original intention on this was if the timer got to 0 and its break time,

        if COUNT % 8 == 0:  # break time should start on its own without having to press the start again
            text.config(text = f"{COUNT}. Long break")  # but i couldn't manage to get it right due to
            count_down(break_timer_count_long)  # me not knowing how to start a timer again after a work session.
        else:
            text.config(text = f"{COUNT}. Break")
            count_down(break_timer_count_short)


def reset():
    global COUNT
    COUNT = 0
    update_checkmarks(check_marks)


# ---------------------------- DISPLAY ------------------------------- #
def return_minutes(time):
    return f"{int(time / 60)}"


def return_seconds(time):
    if len(f"{time % 60}") == 1:  # lol
        return f"0{time % 60}"
    else:
        return f"{time % 60}"


def update_checkmarks(check_mark_label):
    global COUNT

    COUNT += 1
    check_mark_label.config(text = COUNT // 2 * "✓")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time):
    global COUNT, window, canvas

    if time >= 0:
        window.after(1000, count_down, time - 1)  # TODO SET THE UPDATE MS HERE FOR TEST PURPOSES
        canvas.itemconfig(timer_text, text = f"{return_minutes(time)}:{return_seconds(time)}")
        time -= 1

    if time == 0:
        update_checkmarks(check_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomatimer")
window.config(padx = 20, pady = 20, bg = YELLOW)

text = Label(text = "Tomatimer", font = (FONT_NAME, 32, "bold"), bg = YELLOW, fg = GREEN)
text.grid(row = 0, column = 1)

image = PhotoImage(file = "tomato.png")
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
canvas.create_image(100, 112, image = image)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 24, "bold"))
canvas.grid(row = 1, column = 1)

start_button = Button(text = "Start", font = (FONT_NAME, 12, "bold"), bg = PINK, fg = WHITE, command = start)
start_button.grid(row = 2, column = 0)  # TODO add a condition so that if the ongoing timer didn't get down to 0, this button should not be clickable

reset_button = Button(text = "Reset", font = (FONT_NAME, 12, "bold"), bg = PINK, fg = WHITE, command = reset)
reset_button.grid(row = 2, column = 2)  # TODO reset ongoing timer if there is one

# TODO add a pause/resume button, skip current ongoing timer button

check_marks = Label(text = "", font = (FONT_NAME, 10, "bold"), bg = GREEN, fg = YELLOW)
check_marks.grid(row = 3, column = 1)

window.mainloop()
