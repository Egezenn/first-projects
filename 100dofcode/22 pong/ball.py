from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move_amt = 5
        self.y_move_amt = 5

    def move(self):
        self.bounce()
        x = self.xcor() + self.x_move_amt
        y = self.ycor() + self.y_move_amt
        self.goto(x, y)

    def bounce(self):
        if self.ycor() > 280:
            self.y_move_amt *= -1
        elif self.ycor() < -280:
            self.y_move_amt *= -1
