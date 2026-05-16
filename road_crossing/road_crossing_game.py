import turtle
import random

player = Player()
turtle.listen()


turtle.onkey(player.move_up,"Up")
turtle.onkey(player.move_down,"Down")
cars = Car()

turtle.tracer(0)

while True:
    cars.move_up()
    if random.randint(1,100) == 50:
        cars.make_car()
    turtle.update()



turtle.done()
