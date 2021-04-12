def caseSort(s,n):
    s=list(s)
    small=[]
    large=[]
    for i in range(int(n)):
        if s[i]>='A' and s[i]<='Z':
            large.append(s[i])
        if s[i]>='a' and s[i]<='z':
            small.append(s[i])
    small.sort()
    large.sort()
    l=sm=0
    print(small)
    print(large)

    # defRTSersUXI
    for i in range(int(n)):
        if s[i]>='A' and s[i]<='Z':
            s[i]=large[l]
            l+=1
        if s[i]>='a' and s[i]<='z':
            s[i] = small[sm]
            sm += 1
    s = ''.join(map(str, s))
    return s

num = int(input())
for i in range(num):
    n = str(input())
    s = str(input())
    print(caseSort(s,n))