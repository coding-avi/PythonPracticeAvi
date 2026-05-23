# we maek a raer and save the winner in txt file
import turtle
import datetime 
import random

class Racer(turtle.Turtle):
    def __init__(self, color, y_position,name):
        super().__init__()
        self.color(color)
        self.shape("turtle")
        self.penup()
        self.goto(-300, y_position)
        self.name = name

    def move(self):
        self.forward(random.randint(1, 20))


avi = Racer("blue", 100,"avi")
umair = Racer("red", -100,"umair")
jay = Racer("purple", 0,"jay")
turtles = [avi, umair, jay]
flag = ""
while flag != "end":
    for racer in turtles:
        racer.move()
        if racer.xcor() > 300:
            winner = racer.name
            with open("winner.txt", "a") as file:
                file.write(f"The winner at {datetime.datetime.now()}  is: {winner}\n")

            print(f"The winner is: {winner}")
            flag = "end"
            break
            