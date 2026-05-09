import turtle



ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(5)

speedx = 10
speedy = 10
while True:
    ball.goto(ball.xcor() + speedx, ball.ycor() + speedy)
    if ball.xcor()>300:
        speedx = -10
    if ball.xcor()<300:
        speedx = 10
    if ball.ycor()>250:
        speedy = -10
    if ball.ycor()<250:
        speedy = 10
    



turtle.mainloop()