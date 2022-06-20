from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super(Paddle, self).__init__()
        self.penup()
        self.shape("square")
        self.color(128, 128, 255)
        self.turtlesize(1, 5)
        self.setheading(90)

    def moveup(self):
        if self.heading != 90:
            self.setheading(90)
        self.fd(25)

    def movedown(self):
        if self.heading != 270:
            self.setheading(270)
        self.fd(25)
