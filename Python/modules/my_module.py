def sort_list(a):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if(a[i]>a[j]):
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
def reverse_list(a):
    for i in range(0,len(a)//2):
        temp=a[i]
        a[i]=a[len(a)-1-i]
        a[len(a)-1-i]=temp
