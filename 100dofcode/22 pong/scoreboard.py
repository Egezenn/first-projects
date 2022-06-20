from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score1 = 0
        self.score2 = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.appearance()
        self.goto(-40, 240)
        self.write(self.score1, move = False, align = "center", font = ("Arial", 32, "bold"))
        self.goto(40, 240)
        self.write(self.score2, move = False, align = "center", font = ("Arial", 32, "bold"))

    def appearance(self):
        self.hideturtle()
        self.penup()
        self.color(128, 128, 200)
