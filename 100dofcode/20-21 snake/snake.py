from turtle import Turtle

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for x in range(0, 3):
            snakebody = Turtle()
            snakebody.shape("circle")
            snakebody.color(240, 240, 240)
            snakebody.penup()
            snakebody.speed("fastest")
            snakebody.setx(-20 * x)
            self.body.append(snakebody)

    def append_snake(self):
        snakebody = Turtle()
        snakebody.shape("circle")
        snakebody.color(240, 240, 240)
        snakebody.penup()
        snakebody.speed("fastest")
        newx = self.body[-1].xcor()
        newy = self.body[-1].ycor()
        self.body[-1].goto(newx, newy)
        self.body.append(snakebody)

    def move(self):
        for bodies in range(len(self.body) - 1, 0, -1):
            newx = self.body[bodies - 1].xcor()
            newy = self.body[bodies - 1].ycor()
            self.body[bodies].goto(newx, newy)
        self.head.fd(20)

    def keyW(self):
        if self.head.heading() != DOWN:
            if self.head.heading != UP:
                for bodies in self.body:
                    bodies.setheading(UP)

    def keyA(self):
        if self.head.heading() != RIGHT:
            if self.head.heading != LEFT:
                for bodies in self.body:
                    bodies.setheading(LEFT)

    def keyS(self):
        if self.head.heading() != UP:
            if self.head.heading != DOWN:
                for bodies in self.body:
                    bodies.setheading(DOWN)

    def keyD(self):
        if self.head.heading() != LEFT:
            if self.head.heading != RIGHT:
                for bodies in self.body:
                    bodies.setheading(RIGHT)
