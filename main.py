import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
slow_car = CarManager()
fast_car = CarManager()
scoreboard = Scoreboard()
fast_car.generate_starting_cars()
slow_car.generate_starting_cars()

game_is_on = True
clock = 0
slow_speed = 1
fast_speed = 1.5
level = 1

screen.listen()
screen.onkeypress(player.player_move, "space")

while game_is_on:
    clock += 1
    time.sleep(0.01)
    screen.update()

    fast_car.operating_cars_move(slow_speed)
    slow_car.operating_cars_move(fast_speed)
    if clock % 50 == 0:
        slow_car.create_new_car(level)
        if len(fast_car.operating_cars) > 50:
            slow_car.remove_car(level)

    if clock % 180 == 0:
        fast_car.create_new_car(level)
        if len(fast_car.operating_cars) > 50:
            fast_car.remove_car(level)

    if player.ycor() > 300:
        player.next_level()
        slow_speed *= 1.2
        fast_speed *= 1.2
        level += 1

    if fast_car.check_accident(player):
        game_is_on = False

    if slow_car.check_accident(player):
        game_is_on = False

scoreboard.game_over()
screen.exitonclick()
