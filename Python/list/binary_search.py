#Searching:
#Binary search
print("Enter Element in List\n")
a=[int(x) for x in input().split()]
print("Original List is \n",a)
a.sort()
start=0
end=len(a)-1
mid=int((start+end)/2)
n=int(input("Enter the Number to Search in list "))
while(n!=a[mid] and start<=end):
	if(n<a[mid]):
		end=mid-1
	else:
		start=mid+1
	mid=int((start+end)/2)
if(n==a[mid]):
	print(n,"  Exist in List at a[",mid,"]")
else:
	print(n,"Does not Exist in List")
input()

#Time Complexity of Linear Search = O(n)
#Time COmplexity of Binary Search O(log2n): log(n)/log(2)