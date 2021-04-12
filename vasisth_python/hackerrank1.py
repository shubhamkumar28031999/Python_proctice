length=int(input(""))
input_string=input("")
list=input_string.split()
sum=0
for i in list[0:length]:
    sum+=int(i)
print(sum)