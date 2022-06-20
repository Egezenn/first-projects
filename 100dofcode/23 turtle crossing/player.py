from turtle import Turtle
from time import sleep

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.set_player()

    def set_player(self):
        """after clear, redefines what the object is and moves it back to start"""
        self.setheading(90)
        self.shape("turtle")
        self.color(255, 255, 255)
        self.penup()
        self.goto(STARTING_POSITION)

    def finish_state(self, scoreboard, timer):
        """checks if the player is above y=280, updates player location & scoreboard if it is, if it's not adds .1 to timer and sleeps .1 seconds"""
        if self.ycor() >= FINISH_LINE_Y:
            self.clear()
            self.set_player()
            print(f"{scoreboard.level}: {round(timer.timer, 2)}")
            timer.timer = 0
            scoreboard.level += 1
            scoreboard.write_level()
        else:
            timer.timer += 0.1
            sleep(0.1)

    def keypress_w(self):
        """move up"""
        self.setheading(90)
        self.fd(MOVE_DISTANCE)

    def keypress_a(self):
        """move left"""
        self.setheading(180)
        self.fd(MOVE_DISTANCE)
        self.setheading(90)

    def keypress_s(self):
        """move down"""
        self.setheading(270)
        self.fd(MOVE_DISTANCE)
        self.setheading(90)

    def keypress_d(self):
        """move right"""
        self.setheading(0)
        self.fd(MOVE_DISTANCE)
        self.setheading(90)
