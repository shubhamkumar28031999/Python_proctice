import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9]
y=[23,34,24,56,45,67,62,78,89]
plt.scatter(x,y,label='stars',color='green',marker='*',s=70)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.title('scatter plot')
plt.show() 