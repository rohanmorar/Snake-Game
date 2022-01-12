from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard


WIDTH = 600
HEIGHT = 600
EDGE = 280

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake game")
s.tracer(0)

snake = Snake()
food = Food()
sb = Scoreboard()


def game_over_prompt(flag):
    snake.clear_snake()
    s.update()
    food.hide_food()
    sb.lose_msg()
    s.update()
    flag = False

sb.isvisible()
s.onkey(key="Up", fun=snake.up)
s.onkey(key="Left", fun=snake.left)
s.onkey(key="Right", fun=snake.right)
s.onkey(key="Down", fun=snake.down)

game_on = True
while game_on:
    s.update()
    time.sleep(0.1)
    snake.move()
    s.listen()

    if snake.head.distance(food) < 20.0:
        food.refresh()
        sb.add_point()
        snake.extend()

    # detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over_prompt(game_on)

    # detect self collision
    if snake.self_collision():
        game_over_prompt(game_on)











s.exitonclick()
