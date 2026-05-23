import turtle
import random
from games.road_crossing.player import Player
from games.road_crossing.cars import Car


# Setup screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Road Crossing Game")

# Draw finish line
finish_line_turtle = turtle.Turtle()
finish_line_turtle.penup()
finish_line_turtle.goto(-300, 280)
finish_line_turtle.pendown()
finish_line_turtle.pensize(3)
finish_line_turtle.pencolor("green")
finish_line_turtle.goto(300, 280)
finish_line_turtle.penup()
finish_line_turtle.hideturtle()

# Score and level display
score_display = turtle.Turtle()
score_display.penup()
score_display.hideturtle()
score_display.goto(-290, 270)
score_display.color("black")

level = 1
game_is_on = True

player = Player()
cars = Car()
turtle.listen()

turtle.onkey(player.move_up, "Up")
turtle.onkey(player.move_down, "Down")

turtle.tracer(0)

# Game loop
while game_is_on:
    turtle.update()
    
    # Create cars randomly
    if random.randint(1, 500) == 5:
        cars.make_car()
    
    # Move cars
    cars.move_cars()
    
    # Check for collision
    if cars.is_collision(player.player):
        score_display.write("GAME OVER! Hit by a car!", font=("Arial", 16, "normal"))
        game_is_on = False
    
    # Check if player reached finish line
    if player.is_at_finish_line():
        level += 1
        player.reset_position()
        cars.cars = []  # Clear all cars
        score_display.clear()
        score_display.write(f"Level: {level}", font=("Arial", 16, "normal"))

turtle.done()
