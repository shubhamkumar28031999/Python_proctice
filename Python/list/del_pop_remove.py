#all three used to delete any element from list
#pop()
#del
#remove()
a=[10,20,30,40,50,60,70,80,60,90,100]
print("Original List is a =\n",a)
del a[4]
print("List after Deleting 4th index value is a =\n",a)
a.pop()
print("List after pop method is a =\n",a)
a.pop(1)
print("List after pop(index) method is a =\n",a)
a.remove(60)
print("List after remove(element) method is a =\n",a)
input()