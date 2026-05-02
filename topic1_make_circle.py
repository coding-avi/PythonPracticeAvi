import turtle
import random
avi = turtle.Turtle()
avi.shape("turtle")
avi.speed("fastest")

colors= ["yellow","orange","orange","red"]



for i in range(500):
    avi.forward(100)
    avi.left(90)

    avi.forward(100)
    avi.left(90)

    avi.forward(100)
    avi.left(90)

    avi.forward(100)
    avi.left(90)

    
    avi.color(colors[i%4])
    if i >100:
        avi.left(2)
    else:
        avi.right(5)







turtle.mainloop()