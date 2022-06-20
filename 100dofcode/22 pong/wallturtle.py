from turtle import Turtle


class Wallturtle(Turtle):
    def __init__(self):
        super(Wallturtle, self).__init__()
        self.hideturtle()
        self.penup()

    def walls(self):
        self.wall_with_spaces()
        self.pencolor(128, 128, 192)
        self.goto(0, -295)
        self.pendown()
        self.goto(350, -295)
        self.goto(350, 295)
        self.goto(-350, 295)
        self.goto(-350, -295)
        self.goto(0, -295)

    def wall_with_spaces(self):
        self.goto(0, 280)
        self.pencolor(90, 90, 90)
        self.setheading(270)
        self.fd(35)
        self.pendown()
        self.fd(70)
        self.penup()
        self.fd(70)
        self.pendown()
        self.fd(70)
        self.penup()
        self.fd(70)
        self.pendown()
        self.fd(70)
        self.penup()
        self.fd(70)
        self.pendown()
        self.fd(70)
        self.penup()
        self.fd(35)
