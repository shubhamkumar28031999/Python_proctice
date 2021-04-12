# Bubble Sort
a=[]
print("Enter Element in List\n")
for x in range(10):
	a.append=(int)(input('Enter No'))
print("Original List is \n",a)
for i in range(len(a)-1,0,-1):
	for j in range(0,i):
		if(a[j]>a[j+1]):
				temp=a[j]
				a[j]=a[j+1]
				a[j+1]=temp
print("Sorted List is \n",a)




