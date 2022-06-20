# import turtle
# from turtle import *
# import turtle as t
# import turtle
from turtle import Turtle, Screen
import random
import colorgram

jimmy = Turtle()
screen = Screen()
jimmy.speed("fastest")
screen.colormode(255)
jimmy.hideturtle()
jimmy.penup()
dacolors = []

colors = colorgram.extract("image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    dacolors.append((r, g, b))


def draw_lines(dotamount, gap, dotsize):
    randcolor = random.choice(dacolors)
    jimmy.pencolor(randcolor)
    jimmy.dot(dotsize)
    for x in range(dotamount):
        randcolor = random.choice(dacolors)
        jimmy.pencolor(randcolor)
        jimmy.dot(dotsize)
        jimmy.forward(gap)


def square(nxn, gap, dotsize):
    for a in range(1, nxn + 1):
        draw_lines(nxn, gap, dotsize)
        jimmy.sety(a*gap)
        jimmy.setx(0)


square(nxn = 10, gap = 40, dotsize = 30)

screen.exitonclick()

# for x in range(90):
#     jimmy.rt(4)
#     jimmy.circle(200)
#     jimmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# def circle():
#     for x in range(360):
#         jimmy.lt(1)
#         jimmy.fd(2)
# for x in range(12):
#     jimmy.rt(30)
#     circle()
#     jimmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# jimmy.pensize(10)
# directions = [0, 90, 180, 270]
# def pick_dir_fd():
#     jimmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     jimmy.setheading(random.choice(directions))
#     jimmy.fd(20)
# a = 0
# while a != 300:
#     pick_dir_fd()
#     a += 1

# repetitions = 3
# while repetitions != 30:
#     for x in range(repetitions):
#         jimmy.fd(50)
#         jimmy.lt(180 - (repetitions-2)*180/repetitions)
#     screen.colormode(255)
#     jimmy.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     jimmy.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
#     repetitions += 1
# for x in range(10):
#     jimmy.fd(20)
#     jimmy.penup()
#     jimmy.fd(20)
#     jimmy.pendown()

# jimmy.fd(100)
# jimmy.lt(90)
# jimmy.fd(100)
# jimmy.lt(90)
# jimmy.fd(100)
# jimmy.lt(90)
# jimmy.fd(120)
# jimmy.lt(90)
#
# jimmy.fd(100)
# jimmy.rt(90)
# jimmy.fd(100)
# jimmy.rt(90)
# jimmy.fd(100)
# jimmy.rt(90)
# jimmy.fd(120)
#
# jimmy.lt(90)
# jimmy.fd(120)
# jimmy.rt(90)
# jimmy.fd(100)
# jimmy.rt(90)
# jimmy.fd(100)
# jimmy.rt(90)
# jimmy.fd(120)
#
# jimmy.fd(100)
# jimmy.rt(90)
# jimmy.fd(100)
# jimmy.rt(90)
# jimmy.fd(100)
# jimmy.rt(90)
# jimmy.fd(100)
# jimmy.rt(90)
