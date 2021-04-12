import matplotlib.pyplot as plt
activities=['python','C++','Ruby','java']
slices=[215,130,245,210]
colors=['r','g','y','b','m']
explode=(0.1, 0, 0, 0)
plt.pie(slices,labels=activities,colors=colors,startangle=140,autopct='%1.1f%%',shadow=True,explode=explode)
plt.legend()
plt.show()