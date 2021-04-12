def Lapindromes(s):
    l = len(s)
    left_string=[]
    right_string=[]
    if l%2==0:
        left_string.extend(list(s[:int(l/2)]))
        right_string.extend(list(s[int(l/2):]))
    else:
        left_string.extend(list(s[:l//2]))
        right_string.extend(list(s[l//2+1:]))
    left_string.sort()
    right_string.sort()
    if left_string == right_string:
        return True
    else:
        return False


if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=input()
        if Lapindromes(n):
            print("YES")
        else:
            print("NO")

