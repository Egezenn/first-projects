from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.colormode(255)
screen.bgcolor(130, 200, 130)
screen.title("Da Dank Snek Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_continuing = True
while game_is_continuing:
    screen.listen()
    screen.onkey(snake.keyW, "w")
    screen.onkey(snake.keyW, "Up")
    screen.onkey(snake.keyA, "a")
    screen.onkey(snake.keyA, "Left")
    screen.onkey(snake.keyS, "s")
    screen.onkey(snake.keyS, "Down")
    screen.onkey(snake.keyD, "d")
    screen.onkey(snake.keyD, "Right")
    if snake.head.distance(food) < 18:
        food.recreate()
        snake.append_snake()
        scoreboard.scoreupdate()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_continuing = False

    for bodies in snake.body[1:len(snake.body)]:
        if snake.head.distance(bodies) < 10:
            scoreboard.game_over()
            game_is_continuing = False

    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
