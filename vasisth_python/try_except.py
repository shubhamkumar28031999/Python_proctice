a=[]
while(True):
    b=input("enter the number:")
    try:
        if b=='done':break
        a.append(int(b))
    except:
        print('invalid input')
print(f"maximum no. is {max(a)}")
print(f"minimum no. is {min(a)}")

