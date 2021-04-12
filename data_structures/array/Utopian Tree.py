def utopianTree(n):
    heigth=1
    arr=[]
    for i in n:
        for k in range(0,i):
            if k%2==0:
                heigth*=2
            else:
                heigth+=1
        arr.append(heigth)
        heigth=1
    return arr

if __name__=="__main__":
    arr=[6,5,4]
    print(utopianTree(arr))