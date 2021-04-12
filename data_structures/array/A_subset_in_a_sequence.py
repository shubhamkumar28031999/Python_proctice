def substring(n):
    n=bin(n)
    n=n.replace('0b',"")
    d=[]
    for i in range(len(n)):
        if n[i]=='0':
            pass
        else:
            d.append(int(n[i])*(3**(len(n)-i-1)))
    print(len(d))
    print(*d)

if __name__=="__main__":
    for _ in range(int(input())):
        substring(int(input()))
