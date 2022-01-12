from turtle import Turtle,Screen
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.penup()
        self.color("red")
        x1 = random.randint(-275, 275)
        y1 = random.randint(-275, 260)
        self.goto(x1,y1)

    def refresh(self):
        x = random.randint(-275, 275)
        y = random.randint(-265, 275)
        self.goto(x,y)

    def hide_food(self):
        self.hideturtle()






