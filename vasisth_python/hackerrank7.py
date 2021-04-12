no=int(input(""))
marks=[]
for i in range(0,no):
    marks.append(int(input("")))
for i in range(0,no):
    if marks[i]<38:
        marks[i]=marks[i]
    if marks[i]>=38:
        if (((marks[i]//5+1)*5)-marks[i])<3:
            marks[i]=(marks[i]//5+1)*5
        else:
            marks[i] = marks[i]
for i in marks:
    print(i)

