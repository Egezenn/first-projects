from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz_brain = quiz_brain
        self.screen = Tk()
        self.screen.config(padx=20, pady=20, bg=THEME_COLOR)
        self.screen.title("QuizApp")

        img_f = PhotoImage(file="images/false.png")
        img_t = PhotoImage(file="images/true.png")

        self.label = Label(text=f"Score: {self.quiz_brain.score}/{self.quiz_brain.question_number}", fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.text = self.canvas.create_text(150, 125, width=280, text=self.quiz_brain.next_question(), font=("Arial", 20, "italic"), fill="#000000")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=40)

        self.true_button = Button(image=img_t, highlightthickness=0, command=self.true_button)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=img_f, highlightthickness=0, command=self.false_button)
        self.false_button.grid(row=2, column=1)

        self.screen.mainloop()

    def next_question(self):
        if self.quiz_brain.still_has_questions():
            self.canvas.config(bg="white")
            self.canvas.itemconfigure(self.text, text=self.quiz_brain.next_question())
            self.true_button.config(state="active")
            self.false_button.config(state="active")
        else:
            self.screen.destroy()

    def false_button(self):
        if self.quiz_brain.current_question.answer == "False":
            self.quiz_brain.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.label.config(text=f"Score: {self.quiz_brain.score}/{self.quiz_brain.question_number}")
        self.screen.after(1000, self.next_question)

    def true_button(self):
        if self.quiz_brain.current_question.answer == "True":
            self.quiz_brain.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.label.config(text=f"Score: {self.quiz_brain.score}/{self.quiz_brain.question_number}")
        self.screen.after(500, self.next_question)
