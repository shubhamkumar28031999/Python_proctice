import random
num1 = random.randint(0 , 100)

flag = 0
while ( flag <= 5):
    flag += 1
    num2 = int(input("enter any number in between 0 to 100"))
    if num1 == num2:
        print("wow you won the game")
    else:
        if num1 < num2:
            print("you entered a bigger number")
        elif num1 > num2:
            print("you entered a smaller number")



