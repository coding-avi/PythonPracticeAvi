# we make a function that takes two number 
# if first number is bigger then it print big number
# if first number is smaller than second number it prints small
# if first number and second number is same it print same
import random
def first_number_checker (n1,n2):
    if n1 > n2:
        print("number is bigger decrease your number!")
    elif n1 < n2:
        print ("number is smaller increase your number")
    else:
        print("matched")
        return True
    return False   


def random_number_generator(a,b):
    return random.randint(a,b)

def main ():
    # ask computer to genrate rando number
    computer = random_number_generator(1,100)

    for i in range(1,10):
        # please ask user to a nuber from 1 to 100
        user = int(input("please pic a number 1 to 100:"))
        apple = first_number_checker(user,computer)
        if apple ==True:
            break
        
    print("the number was",computer)


main()