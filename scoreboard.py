from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def lose_msg(self):
        m = Turtle()
        m.penup()
        m.goto(0,0)
        m.color("white")
        m.write("GAME OVER", False, align=ALIGN, font=FONT)
        m.hideturtle()










