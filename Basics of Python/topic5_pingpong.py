import turtle

rod_left = turtle.Turtle("square")
rod_left.penup()
rod_left.shapesize(5,1)
rod_left.goto(400,0)



rod_right = turtle.Turtle("square")
rod_right.penup()
rod_right.shapesize(5,1)
rod_right.goto(-400,0)



def left_up():
    rod_left.goto(rod_left.xcor(),rod_left.ycor()-20)

def left_down():
    rod_left.goto(rod_left.xcor(),rod_left.ycor()-20)

def right_up():
    rod_right.forward(rod_right.xcor(),rod_right.ycor()+20)

def right_down():
    rod_right.forward(rod_right.xcor(),rod_right.ycor()-20)


turtle.listen()
turtle.onkey(left_up,"w")
turtle.onkey(left_down,"s")
turtle.onkey(right_up,"Up")
turtle.onkey(right_down,"Down")







turtle.mainloop()




