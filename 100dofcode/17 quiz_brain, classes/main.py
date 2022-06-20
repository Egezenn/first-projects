from data import *
from question_model import *
from quiz_brain import *
import random

# old
# question_bank = []
#
# for questions in question_data:
#     question = Question(questions["text"], questions["answer"])
#     question_bank.append(question)
#
# quiz = QuizBrain(question_bank)
# while quiz.questions_left() == True:
#     quiz.next_question()
# if quiz.question_number == len(question_data):
#     print(f"You've completed the quiz with a score of {quiz.score}/{quiz.question_number}")

question_bank = []


for questions in question_data_expanded:
    question = QuestionExpanded(questions["category"], questions["difficulty"], questions["question"], questions["correct_answer"])
    question_bank.append(question)

random.shuffle(question_bank)

quiz = QuizBrainExpanded(question_bank)
while quiz.questions_left():
    quiz.next_question()

if quiz.question_number == len(question_data_expanded):
    print(f"You've completed the quiz with a score of {quiz.score}/{quiz.question_number}")


# uhh
# def generate_question():
#     randint = random.randint(0, 11)
#     return Question((question_data[randint]["text"]), (question_data[randint]["answer"]))
#
# def game():
#     score = 0
#     questionnum = 0
#     questionlist = []
#     for x in range(0, 3):
#         questionlist.append(generate_question())
#
#     while questionlist[0] == questionlist[1] or questionlist == questionlist[2] or questionlist[1] == questionlist[2]:
#         questionlist.clear()
#         for x in range(0, 3):
#             questionlist.append(generate_question())
#
#     while score != 3 and score != -1:
#         question = questionlist[score]
#         choice = input(f"{question.text}: ").title()
#         if choice == question.answer:
#             score += 1
#             questionnum += 1
#             print(f"Correct! {score}/3\n")
#         else:
#             print(f"Incorrect! {score}/3\n")
#             score = -1
#         if score == 3:
#             print("You won!")
#
# bye = "nope"
# while bye == "nope":
#     game()
#     bye = input("Play again? y or n: ").lower()
#     print()
#     if bye == "y":
#         bye = "nope"
