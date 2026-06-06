import turtle

turtles = [turtle.Turtle(shape="turtle"), turtle.Turtle(shape="turtle"), turtle.Turtle(shape="turtle"), turtle.Turtle(shape="turtle"), turtle.Turtle(shape="turtle")]

turtles[0].color("red")
turtles[1].color("green")
turtles[2].color("blue")
turtles[3].color("yellow")
turtles[4].color("purple")


while True:
    x = int(input("Enter the turtle number (0-4) to move, or -1 to exit: "))
    y = int(input("Enter the distance to move the turtle: "))
    z = int(input("Enter the direction to move the turtle (0 to 360): "))
    if x == -1:
        break
    if 0 <= x < len(turtles):
        turtles[x].setheading(z)
        turtles[x].forward(y)
    else:
        print("Invalid turtle number. Please enter a number between 0 and 4.")
    