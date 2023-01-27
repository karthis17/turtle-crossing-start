from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level_point = 0
        self.goto(-250, 250)
        self.level_bord()

    def level_bord(self):
        self.clear()
        self.write(f"Level : {self.level_point}", align="left", font=FONT)

    def level_increment(self):
        self.level_point += 1
        self.level_bord()

    def GameOver(self):
        self.goto(0, 0)
        self.write(f"""Game Over
        Score : {self.level_point}""", align="center", font=FONT)


