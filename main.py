import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move_forward, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.carMove()
    if player.reach_finishing_line():
        scoreboard.level_increment()
        player.go_back()
        car.refresh()
    for cars in car.cars:
        if cars.distance(player) < 20:
            scoreboard.GameOver()
            game_is_on = False

screen.exitonclick()
