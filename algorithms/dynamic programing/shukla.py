if __name__=="__main__":
    input1=int(input())
    arr=list(map(int,input().strip().split()))
    input3=int(input())
    list1=[]
    list1.append(arr[0]+arr[1])
    for i in range(2,len(arr)):
        list1.append(arr[i]+list1[-1])
    product1 =1
    for j in range(len(list1)):
        product1*=list1[j]
    arr=arr[::-1]
    list2 = []
    list2.append(arr[0] + arr[1])
    for i in range(2, len(arr)):
        list2.append(arr[i] + list2[-1])
    product2 = 1
    for j in range(len(list2)):
        product2 *= list2[j]
    min_val=min(product1,product2)
    print(min_val)