from random import randint
c=15
num=randint(1,20000)
while(c>0):
    input("Press any Kry to Continue..........")
    print("\n\n\n\n")
    print("Gues a Number in Range 1 to 20000 : ")
    print("Chance Left ",c)
    user=int(input())
    if(user==num):
         print("You Won!!!!!!!!!!")
         print("Chance Still Left :  ",c)
         break
    else:
        c=c-1

    if(c==0):
        print("You Lost !!!!!!!!!!")
        print("Number is ",num)
        break
    elif(user<num):
        print("Number is Greater")
    else:
        print("Number is Smaller")
input()

    
