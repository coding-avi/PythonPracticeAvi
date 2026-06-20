import math
import turtle


avi = turtle.Turtle()

for i in range(-300,300,1):
    avi.goto(i, 100* math.sin(i / 10) )

turtle.mainloop()