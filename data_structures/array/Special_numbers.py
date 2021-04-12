from itertools import product
def powerset(string,low,high,min_val,max_val):
    l=[]
    count=0
    for i in range(low,high+1):
        for element in product(string,repeat=i):
            temp_val=int(''.join(element))
            if temp_val in l:
                pass
            else:
                if temp_val>=min_val and temp_val<=max_val:
                    l.append(temp_val)
                    count+=1
    return count
if __name__=="__main__":
    for _ in range(int(input())):
        low,high,divisor=list(map(int,input().strip().split()))
        arr=[]
        for i in range(0,10):
            if i%divisor==0:
                arr.append(str(i))
        print(powerset(arr,len(str(low)),len(str(high)),int(low),int(high)))






