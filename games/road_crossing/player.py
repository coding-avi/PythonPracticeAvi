
import turtle

class Player():
    def __init__(self):
        self.player = turtle.Turtle("turtle")
        self.player.penup()
        self.player.setheading(90)
        self.player.goto(0, -280)
        self.player.shapesize(1, 1)
        self.player.color("orange")

    def move_up(self):
        new_y = self.player.ycor() + 20
        if new_y < 300:  # Don't go off top
            self.player.goto(self.player.xcor(), new_y)

    def move_down(self):
        new_y = self.player.ycor() - 20
        if new_y > -300:  # Don't go off bottom
            self.player.goto(self.player.xcor(), new_y)

    def is_at_finish_line(self):
        """Check if player reached the top"""
        return self.player.ycor() > 280

    def reset_position(self):
        """Reset player to starting position"""
        self.player.goto(0, -280)



