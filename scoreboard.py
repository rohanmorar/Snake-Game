from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.read_hs()
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.read_hs()
        self.update_scoreboard()
        self.hideturtle()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_hs(self.highscore)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write("Score: {} | Highscore: {}".format(self.score,self.highscore), align=ALIGN, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def save_hs(self,curr_hs):
        with open("data.txt", mode="a") as myf:
            new_hs = str(curr_hs)
            myf.write(f"\n{new_hs}")

    def read_hs(self):
        with open("data.txt", mode="r") as myf:
            contents = myf.read()
            for line in contents:
                if line[-1:].isdigit():
                    result = int(line[-1:])
            self.highscore = int(result)
        myf.close()













