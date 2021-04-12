def nonDivisibleSubset(a, s):
    length=len(s)
    arr=set()
    for i in range(length-1):
        for k in range(i+1,length):
            if (s[i]+s[k])%a!=0:
                print()
                arr.add(s[i])
                arr.add(s[k])
            print(f"{s[i]} + {s[k]} = {s[i] + s[k]} -------> {(s[i] + s[k]) % a} ---->{arr}")
    return len(arr)


if __name__=="__main__":
    k=9
    arr=[422346306,940894801,696810740,862741861,85835055,313720373]
    print(nonDivisibleSubset(k,arr))