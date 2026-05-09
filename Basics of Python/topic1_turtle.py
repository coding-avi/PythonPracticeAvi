import turtle

name1 = "avi"
name2 = "umair"

color1 = "orange"
color2 = "blue"


size1 = 2
size2 = 2

shape1 = "arrow"
shape2 = "circle"

step1 = 100
step2=50


angle1 = 90
angele2 = 120


avi = turtle.Turtle(shape1)
umair = turtle.Turtle(shape2)

avi.shapesize(size1)
umair.shapesize(size2)

avi.forward(step1)
umair.left(90)
umair.forward(100)

turtle.mainloop()