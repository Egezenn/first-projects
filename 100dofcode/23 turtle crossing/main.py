from random import randint
from turtle import Screen
from player import Player
from carmanager import CarManager, STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from scoreboard import Scoreboard

# TODO get timers' print data into a list and add another scoreboard object & make it write every single level time in an ascending order after the timer


def collision(turtle, carlist):
    """checks if the player has hitten a wall or a car"""
    for carx in carlist:
        if turtle.distance(carx) <= 20:
            turtle.set_player()
            if scoreboard.level != 1:
                scoreboard.level -= 1
                scoreboard.write_level()
    if turtle.xcor() > 280 or turtle.xcor() < -280 or turtle.ycor() < -280:
        print("You're smart aren't you.")
        turtle.set_player()


screen = Screen()
screen.setup(width = 600, height = 600)
screen.colormode(255)
screen.bgcolor(0, 0, 0)
screen.tracer(0)

cars = []
player = Player()
scoreboard = Scoreboard()
scoreboard.write_level()
timer = Scoreboard()


while True:
    timer.write_timer()
    screen.listen()
    screen.onkey(player.keypress_w, "w")
    screen.onkey(player.keypress_a, "a")
    screen.onkey(player.keypress_s, "s")
    screen.onkey(player.keypress_d, "d")

    # spawns cars
    while len(cars) <= 50 and player.ycor() <= 280 and randint(0, 6) == 0:

        car = CarManager()
        cars.append(car)

    # sets car move distance
    if scoreboard.level > 1:
        movedistance = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (scoreboard.level - 1)
    else:
        movedistance = STARTING_MOVE_DISTANCE

    # car.state but for every car on the screen
    for car in cars:
        car.state(cars, car, movedistance)

    collision(player, cars)
    player.finish_state(scoreboard, timer)
    screen.update()
