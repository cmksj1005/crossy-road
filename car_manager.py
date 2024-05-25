from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
NUM_OF_STARTING_CARS = 10
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.setheading(180)
        self.penup()
        self.color(COLORS[random.randint(0, 4)])
        self.goto(600, 0)
        self.operating_cars = []

    def generate_starting_cars(self):
        for _ in range(NUM_OF_STARTING_CARS):
            position_x = random.randint(-280, 280)
            position_y = random.randint(-250, 280)
            new_car = CarManager()
            new_car.goto(position_x, position_y)
            self.operating_cars.append(new_car)

    def car_move(self, speed):
        self.forward(speed)

    def operating_cars_move(self, speed):
        for index in range(len(self.operating_cars)):
            self.operating_cars[index].car_move(speed)

    def create_new_car(self, num):
        for _ in range(num):
            new_car = CarManager()
            position_x = random.randint(280, 600)
            position_y = random.randint(-250, 280)
            new_car.goto(position_x, position_y)
            self.operating_cars.append(new_car)

    def remove_car(self, num):
        for _ in range(num):
            self.operating_cars.pop(0)

    def check_accident(self, player):
        for car in self.operating_cars:
            if player.distance(car) < 20:
                return True
        return False
