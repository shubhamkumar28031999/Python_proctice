name,age=input('enter your name and age').split(",")
if (name[0]=='a' or name[0]=='A') and int(age)>=19:
    print("you are eligible")
else :
    print('you are not eligible')
