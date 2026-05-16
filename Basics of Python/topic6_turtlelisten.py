import turtle


class Player:
    def __init__(self,color):
        self.player = turtle.Turtle()
        self.player.color(color)
        self.player.shape("turtle")
    def move(self):
        self.player.forward(20)
    def move_left(self):
        self.player.left(90)
    def move_right(self):
        self.player.right(90)

    


p1 = Player("red")
p2 = Player("blue")

turtle.listen()
turtle.onkeypress(p1.move,"w")
turtle.onkeypress(p2.move,"Up")
turtle.onkeypress(p1.move_left,"a")
turtle.onkeypress(p1.move_right,"d")
turtle.onkeypress(p2.move_left,"Left")
turtle.onkeypress(p2.move_right,"Right")





turtle.mainloop()



