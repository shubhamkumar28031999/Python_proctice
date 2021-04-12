import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open('test1.txt','r') as csvfile:
    plots=csv.reader(csvfile)
    for col in plots:
        x.append(col[0])
        y.append(col[1])


plt.plot(x,y,label='file')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("taking input from file")
plt.show()