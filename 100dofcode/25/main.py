import pandas
import turtle as t

screen = t.Screen()
screen.title("US of A States Game")
screen.addshape("blank_states_img.gif")
t.shape("blank_states_img.gif")

jimmy = t.Turtle()
jimmy.penup()
jimmy.hideturtle()
jimmy.color("green")

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
answer_list = []
score = 0

while len(answer_list) <= 60:
    answer = screen.textinput(f"Score: {score}/50", f"Guesses: {len(answer_list)}\nWhat's another state name?").title()
    answer_list.append(answer)

    if answer == "Exit":
        break

    nmbr = 0  # this number is used to keep track of which element the loop is on and get the answers x, y from a list if the answer is correct
    for states in state_list:
        if answer == states and answer_list.count(answer) <= 1:
            score += 1
            jimmy.goto(data.x.to_list()[nmbr], data.y.to_list()[nmbr])
            jimmy.write(f"{answer}", move=False, align="center", font=("Arial", 8, "normal"))
        nmbr += 1

jimmy.color("purple")
jimmy.home()
if score == 50:
    jimmy.write(f"You won with {len(answer_list)} guesses!", move=False, align="center", font=("Arial", 16, "normal"))
else:
    jimmy.write(f"You lost!", move=False, align="center", font=("Arial", 16, "normal"))
    

    not_guessed = [state for state in state_list if state not in answer_list]
    new_data = pandas.DataFrame(not_guessed)
    
    new_data.to_csv("states_to_learn.csv")

t.mainloop()
