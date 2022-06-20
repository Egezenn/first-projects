from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.appearance()

    def scoreupdate(self):
        self.score += 1
        self.clear()
        self.appearance()

    def appearance(self):
        self.hideturtle()
        self.penup()
        self.color(255, 255, 255)
        self.goto(-290, 275)
        self.write(f"Score: {self.score}", move = True, align = "left", font = ("Arial", 16, "bold"))

    def game_over(self):
        self.clear()
        self.home()
        self.penup()
        self.write(f"Game over!\nYour score was {self.score}", move = False, align = "center", font = ("Arial", 16, "bold"))
