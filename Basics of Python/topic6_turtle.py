import turtle


class Player:
    def __init__(self,color):
        self.player = turtle.Turtle()
        self.player.color(color)
        self.player.shape("turtle")

    


p1 = Player("red")
p2 = Player("blue")
p3 = Player("green")

while True:
    x = int(input("whichturtle you want to move 1 2 or 3: "))
    y = int(input("how many steps? 10 100 200: "))
    if x ==1:
        p1.player.forward(y)
    elif x ==2:
        p2.player.forward(y)
    elif x ==3:
        p3.player.forward(y)
    else:
        print("wrote number try again")

turtle.mainloop()



