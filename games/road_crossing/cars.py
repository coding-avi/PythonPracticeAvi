
import turtle
import random


class Car():
    def __init__(self):
        self.cars = []
        
    def make_car(self):
        """Create a new car at a random height"""
        car = turtle.Turtle("square")
        car.penup()
        car.goto(-300, random.randint(-250, 250))
        car.shapesize(1, 2)
        car.setheading(0)
        car.color(random.choice(["red", "blue", "green", "yellow", "purple"]))
        self.cars.append(car)

    def move_cars(self):
        """Move all cars to the right and remove off-screen cars"""
        for car in self.cars:
            car.forward(0.1)
        
        # Remove cars that have gone off screen
        self.cars = [car for car in self.cars if car.xcor() < 320]

    def is_collision(self, player_turtle):
        """Check if any car collided with the player"""
        for car in self.cars:
            # Check distance between car and player
            distance = ((car.xcor() - player_turtle.xcor()) ** 2 + 
                       (car.ycor() - player_turtle.ycor()) ** 2) ** 0.5
            if distance < 20:
                return True
        return False

