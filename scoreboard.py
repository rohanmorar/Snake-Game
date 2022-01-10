from turtle import Turtle
from food import Food


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def add_point(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 24, "normal"))










