def greeting(name):
    print(f"heyyy {name}! welcome to class")


def age1(age):
    if age >= 18:
        print("you can apply for driving license")
    else:
        print("sorry you are too young")


def draw_sqaure(tt,steps):
    tt.forward(steps)
    tt.left(90)
    tt.forward(steps)
    tt.left(90)
    tt.forward(steps)
    tt.left(90)
    tt.forward(steps)
    tt.left(90)