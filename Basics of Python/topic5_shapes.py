import turtle
from fun import draw_sqaure

avi = turtle.Turtle()
avi.penup()
avi.color("blue")
avi.shape("square")
avi.goto(-300,100)



umair = turtle.Turtle()
umair.shape("circle")
umair.color("red")
umair.penup()
umair.goto(-300,-100)



draw_sqaure(avi,100)
draw_sqaure(umair,50)




turtle.mainloop()