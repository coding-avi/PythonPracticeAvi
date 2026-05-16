
import turtle
class Player():
    def __init__(self):
        self.player = turtle.Turtle("turtle")
        self.player.penup()
        self.player.setheading(90)
        self.player.backward(300)
        self.player.shapesize(3,3)
        self.player.color("orange")

    def move_up(self):
        self.player.goto(self.player.xcor(),self.player.ycor()+20)

    def move_down(self):
        self.player.goto(self.player.xcor(),self.player.ycor()-20)



