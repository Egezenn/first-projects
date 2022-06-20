import random
from turtle import Turtle, Screen


screen = Screen()
screen.colormode(255)
numbero = 0
someothernumber = 1
# these numbers get used to keep track of turtle numbers in for loops, idrk a better way to do it
# there is vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# angela uses turtles pencolors, maybe i'll implement it that way later on
# since i don't use colors i'll just use the terminal to make a bet
# she also uses turtles xcoordinates to find out who is the winner while i'm here trying to do it with a list xd
# downside of that is, she didn't do an exact check of who is the farthest, if it finds one that's far away from the
# specified number, it just quits but never checks others whether or not they're farther from that one
# TODO total redo sometime
# i should really wait 'til i get specifics of the project


def start(turtlelist, number):
    for turtle in turtlelist:
        turtle.shape("turtle")
        turtle.color((random.randint(0, 255)), random.randint(0, 255), random.randint(0, 255))
        turtle.penup()
        turtle.setx(-400)
        turtle.sety(60 + number * -30)
        number += 1


def randommovement(turtlelist, scorelist):
    numberrrr = 0
    for turtle in turtlelist:
        randnumber = random.randint(1, 40)
        turtle.fd(randnumber)
        scorelist[numberrrr] += randnumber
        numberrrr += 1


t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()

turtles = [t1, t2, t3, t4, t5]
scores = [0, 0, 0, 0, 0]

start(turtles, numbero)
user_bet = int(input("Who ya bettin on son?\n"))

# is there a better way of checking this?
while scores[0] < 600 and scores[1] < 600 and scores[2] < 600 and scores[3] < 600 and scores[4] < 600:
    randommovement(turtles, scores)

for score in scores:
    if score > 600:
        if max(scores) == score:
            print(f"Turtle no.{someothernumber} has won!: {score}")
            if someothernumber == user_bet:
                print("You won the bet!")
            else:
                print("You lost the bet!")
            someothernumber += 1
        else:
            print(f"Turtle no.{someothernumber}: {score}")
            someothernumber += 1
    else:
        print(f"Turtle no.{someothernumber}: {score}")
        someothernumber += 1
screen.exitonclick()

# t = Turtle()
# screen = Screen()
# screen.colormode(255)
#
#
# t.pensize(3)
# t.speed("fastest")
# t.hideturtle()
#
# def w():
#     t.setheading(90)
#     t.pencolor((random.randint(0, 255)), random.randint(0, 255), random.randint(0, 255))
#     t.fd(20)
#
# def a():
#     t.setheading(180)
#     t.pencolor((random.randint(0, 255)), random.randint(0, 255), random.randint(0, 255))
#     t.fd(20)
#
# def s():
#     t.setheading(270)
#     t.pencolor((random.randint(0, 255)), random.randint(0, 255), random.randint(0, 255))
#     t.fd(20)
#
# def d():
#     t.setheading(0)
#     t.pencolor((random.randint(0, 255)), random.randint(0, 255), random.randint(0, 255))
#     t.fd(20)
#
# def c():
#     t.clear()
#     t.penup()
#     t.home()
#     t.pendown()
#
# screen.listen()
# screen.onkey(w, "w")
# screen.onkey(a, "a")
# screen.onkey(s, "s")
# screen.onkey(d, "d")
# screen.onkey(c, "c")
#
# screen.exitonclick()
