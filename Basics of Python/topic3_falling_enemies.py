import turtle, random, time

player = turtle.Turtle()
player.color("blue")
player.shape("circle")
player.shapesize(2,2)
player.penup()
player.goto(0,-250)

turtle.listen()
turtle.onkeypress(lambda:player.forward(35),"Right")
turtle.onkeypress(lambda:player.forward(-35),"Left")
a = ["red","yellow","orange","maroon","brown"]

enemies = []
forever = True
spawn_speed = 0.5
time_of_creating = 0.1
start_time = time.time()
turtle.tracer(0)
while forever:
    diff_of_time = time.time() - start_time
    if diff_of_time > time_of_creating:
        enemy = turtle.Turtle()
        enemy.color(random.choice(a))
        enemy.shape("circle")
        enemy.shapesize(2,2)
        enemy.penup()
        enemy.goto(random.randint(-300,300),300)
        enemies.append(enemy)
        start_time = time.time()

    for enemy in enemies:
        enemy.sety(enemy.ycor()-spawn_speed)
        if enemy.distance(player)<30:
            forever = False
            print("game oover")
    turtle.update()



turtle.mainloop()