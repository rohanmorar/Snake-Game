from turtle import Turtle


START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POSITIONS:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(pos)
            self.segments.append(segment)

    def move(self):
        for seg_index in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_index-1].xcor()
            new_y = self.segments[seg_index-1].ycor()
            self.segments[seg_index].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def pstn(self):
        return self.head. position()

    def right(self):
        self.head.setheading(RIGHT)

    def left(self):
        self.head.setheading(LEFT)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)





