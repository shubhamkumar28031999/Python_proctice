for _ in range(int(input())):
    s=input()
    l=len(s)
    prev="0"
    count=0
    for i in range(l):
        if prev=="0" and s[i]=="1":
            count+=1
        prev=s[i]
    print(count)