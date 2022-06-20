from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from wallturtle import Wallturtle
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.colormode(255)
screen.setup(800, 600)
screen.title("PaPaPong")

paddle1 = Paddle()
paddle1.setx(-350)
paddle2 = Paddle()
paddle2.setx(350)

ball = Ball()

wallturtle = Wallturtle()
wallturtle.walls()

scoreboard = Scoreboard()


def refresh():
    scoreboard.score_update()
    paddle1.setx(-350)
    paddle2.setx(350)


while True:
    score = scoreboard.score1 + scoreboard.score2
    if score == 5:  # BO5, could add an input to set it
        if scoreboard.score1 > scoreboard.score2:
            print("P1 has won!")
        elif scoreboard.score1 < scoreboard.score2:
            print("P2 has won!")

        scoreboard.score1 = 0
        scoreboard.score2 = 0
        refresh()

    screen.update()
    screen.listen()
    screen.onkey(paddle1.moveup, "w")
    screen.onkey(paddle1.movedown, "s")
    screen.onkey(paddle2.moveup, "Up")
    screen.onkey(paddle2.movedown, "Down")

    if ball.distance(paddle1) <= 51 and -350 <= ball.xcor() <= -330:
        ball.x_move_amt *= -1
    elif ball.distance(paddle2) <= 51 and 350 >= ball.xcor() >= 330:
        ball.x_move_amt *= -1

    if ball.xcor() >= 350:
        scoreboard.score1 += 1
        ball.goto(0, 0)
        ball.x_move_amt *= -1
        ball.y_move_amt *= -1
        refresh()

    elif ball.xcor() <= -350:
        scoreboard.score2 += 1
        ball.goto(0, 0)
        ball.x_move_amt *= -1
        ball.y_move_amt *= -1
        refresh()

    ball.move()

    speed = 1
    if score != 0:
        speed *= 0.7 ** score
    time.sleep(0.02 * speed)
