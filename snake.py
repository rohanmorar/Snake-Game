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
            self.add_segment(pos)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("spring green")
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def clear_snake(self):
        for seg in self.segments:
            seg.hideturtle()

    def move(self):
        for seg_index in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_index-1].xcor()
            new_y = self.segments[seg_index-1].ycor()
            self.segments[seg_index].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def self_collision(self):
        for i in range(len(self.segments)-1,0,-1):
            if self.head.distance(self.segments[i]) < 10:
                return True
        return False






    def right(self):
        self.head.setheading(RIGHT)

    def left(self):
        self.head.setheading(LEFT)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)





