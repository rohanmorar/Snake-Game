from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake game")
s.tracer(0)

snake = Snake()
food = Food()
sb = Scoreboard()


sb.isvisible()
s.onkey(key="Up", fun=snake.up)
s.onkey(key="Left", fun=snake.left)
s.onkey(key="Right", fun=snake.right)
s.onkey(key="Down", fun=snake.down)

play = True

while play:
    s.update()
    time.sleep(0.1)
    s.listen()

    if snake.head.distance(food) < 20.0:
        food.refresh()
        sb.add_point()

    snake.move()





s.exitonclick()
