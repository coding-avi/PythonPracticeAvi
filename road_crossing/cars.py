
import turtle
import random


class Car():
    def __init__(self):
        self.cars = []
        

    def make_car(self):
        car = turtle.Turtle("turtle")
        car.penup()
        car.goto(-400,random.randint(-400,400))
        car.shapesize(3,3)
        car.color("red")
        self.cars.append(car)

    def move_up(self):
        for car in self.cars:
            car.forward(1)

