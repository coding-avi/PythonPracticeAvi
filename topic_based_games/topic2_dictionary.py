import +math
import random
import turtle

RADIUS = 300
COLORS = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan"]

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Circle Winner Challenge")
screen.tracer(0)

boundary = turtle.Turtle(visible=False)
boundary.color("white")
boundary.pensize(2)
boundary.penup()
boundary.goto(0, -RADIUS)
boundary.pendown()
boundary.circle(RADIUS)

all_turtles = {}
for color in COLORS:
    t = turtle.Turtle(shape="turtle")
    t.color(color)
    t.penup()

    angle = random.randint(0, 360)
    distance = random.randint(10, RADIUS - 30)
    x = distance * math.cos(math.radians(angle))
    y = distance * math.sin(math.radians(angle))
    t.goto(x, y)
    t.setheading(random.randint(0, 360))
    all_turtles[color] = t

message = turtle.Turtle(visible=False)
message.penup()
message.color("white")
message.hideturtle()

winner = None


def outside_circle(turtle_obj):
    return turtle_obj.distance(0, 0) > RADIUS


while len(all_turtles) > 1:
    turtles_to_remove = []

    for color, t in list(all_turtles.items()):
        t.setheading(random.randint(0, 360))
        t.forward(random.randint(3, 8))

        if outside_circle(t):
            turtles_to_remove.append(color)
            t.hideturtle()

    for color in turtles_to_remove:
        all_turtles.pop(color, None)

    screen.update()

if all_turtles:
    winner = next(iter(all_turtles))

message.goto(0, 260)
message.write(f"Winner: {winner.capitalize()} turtle", align="center", font=("Arial", 18, "bold"))
print(f"The winner is the {winner} turtle.")

turtle.done()
