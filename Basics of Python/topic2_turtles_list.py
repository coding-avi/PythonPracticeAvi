import turtle
import random


colors = ["red","blue","orange","purple","indigo","cyan","green","pink",]
y = -300
turtles = []
for color in colors:
    avi = turtle.Turtle()
    avi.penup()
    avi.color(color)
    avi.shape("turtle")
    avi.goto(-380,y)
    y = y + 50
    turtles.append(avi)


while True:
    for each in turtles:
        each.forward(random.randint(1,10))
        if each.xcor()>380:
            turtle.done()




turtle.mainloop()