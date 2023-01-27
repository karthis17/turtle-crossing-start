import random
from turtle import Turtle, Screen

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.screen = Screen()
        self.starting_stage = 5

    def generate_car(self):
        car_time_create = random.randint(1, 6)
        if car_time_create == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 3)
            car.penup()
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def carMove(self):
        for i in self.cars:
            i.forward(self.starting_stage)

    def refresh(self):
        self.starting_stage += MOVE_INCREMENT




