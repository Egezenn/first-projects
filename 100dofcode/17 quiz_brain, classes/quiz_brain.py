class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {current_question.text} (t/f):")
        if choice == "t":
            choice = "True"
        elif choice == "f":
            choice = "False"

        if self.answer_check(choice, current_question.answer) == "correct":
            self.score += 1
            print(f"Correct! {self.score}/{self.question_number}")
        else:
            print(f"Incorrect! {self.score}/{self.question_number}")

    def questions_left(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def answer_check(self, choice, answer):
        if choice == answer:
            return "correct"
        else:
            return "incorrect"


class QuizBrainExpanded:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}\n{current_question.category}\nDifficulty: {current_question.difficulty.title()}\n{current_question.question}\n(t/f): ")
        if choice == "t":
            choice = "True"
        elif choice == "f":
            choice = "False"

        if self.answer_check(choice, current_question.answer) == "correct":
            self.score += 1
            print(f"Correct! {self.score}/{self.question_number}\n")
        else:
            print(f"Incorrect! {self.score}/{self.question_number}\n")

    def questions_left(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def answer_check(self, choice, answer):
        if choice == answer:
            return "correct"
        else:
            return "incorrect"
