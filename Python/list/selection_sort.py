#sorting alogirthms
#Selection sort
#Bubble Sort
#Insertion Sort
#Quick Sort
#Merge Sort
#Heap Sort

# Selection Sort
print("Enter Element in List\n")
a=[int(x) for x in input().split()]
print("Original List is \n",a)
for i in range(0,len(a)-1):
	for j in range(i+1,len(a)):
		if(a[i]>a[j]):
				temp=a[i]
				a[i]=a[j]
				a[j]=temp
print("Sorted List is \n",a)
input()
