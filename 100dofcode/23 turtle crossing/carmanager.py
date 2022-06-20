from turtle import Turtle
from random import randint
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


def generate_color():
    """returns a tuple of color that are neither too dark or too bright"""
    return randint(63, 191), randint(63, 191), randint(63, 191)


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.setheading(180)
        self.color(generate_color())
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.goto(randint(270, 291), randint(-240, 241))

    def state(self, carlist, list_element, distance):
        """checks for cars' x coord, if its below or equal to 290 the car gets removed, else the car moves"""
        if self.xcor() <= -290:
            self.hideturtle()
            carlist.remove(list_element)
        else:
            self.fd(distance)
