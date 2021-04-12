s = input()
arr=s.split(" ")
temp=[]
resutlt=""
for name in arr:
    temp.append(name.capitalize())
for name in temp:
    resutlt=resutlt+name+" "

print(resutlt)