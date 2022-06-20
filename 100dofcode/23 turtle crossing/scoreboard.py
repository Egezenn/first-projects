from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.set_scoreboard()
        self.level = 1
        self.timer = 0

    def set_scoreboard(self):
        """after clear, redefines what the object is"""
        self.hideturtle()
        self.penup()
        self.color(255, 255, 255)

    def write_level(self):
        """used for writing the level"""
        self.clear()
        self.set_scoreboard()
        self.goto(-300, 260)
        self.write(f"Level: {self.level}", False, "left", ("Arial", 28, "normal"))
        self.timer = 0

    def write_timer(self):
        """used for writing the timer"""
        self.clear()
        self.set_scoreboard()
        self.goto(-295, 230)
        self.write(f"Time: {round(self.timer, 1)}", False, "left", ("Arial", 20, "normal"))