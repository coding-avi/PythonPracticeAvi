import turtle
avi = turtle.Turtle("turtle")
avi.speed("fastest")



for i in range(360):
    avi.forward(1)
    avi.left(1)


avi.right(90)
avi.forward(100)
avi.left(45)
avi.forward(70)
avi.forward(-70)

avi.right(90)
avi.forward(70)
avi.forward(-70)


avi.left(45)
avi.forward(-50)

avi.left(90)
avi.forward(60)
avi.forward(-120)



avi.penup()
avi.goto(100,100)
avi.pendown()
for i in range(360):
    avi.forward(1)
    avi.left(1)


avi.right(90)
avi.forward(100)
avi.left(45)
avi.forward(70)
avi.forward(-70)

avi.right(90)
avi.forward(70)
avi.forward(-70)


avi.left(45)
avi.forward(-50)

avi.left(90)
avi.forward(60)
avi.forward(-120)



turtle.mainloop()