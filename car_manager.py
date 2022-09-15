from random import choice, randint
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.pu()
            car.shape("square")
            car.shapesize(1, 2)
            car.color(choice(COLORS))
            starting_y = randint(-250, 250)
            car.goto(325, starting_y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
