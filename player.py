from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_back()
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def go_back(self):
        self.goto(STARTING_POSITION)

    def reach_finishing_line(self):
        if self.ycor() >= 280:
            return True
        else:
            return False
