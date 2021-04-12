def function(s):
    s=s.replace('-',"")
    s=s.replace(" ","")
    l=len(s)
    i=0
    while l>4:
        i+=3
        s=s[:i]+"-"+s[i:]
        i+=1
        l=l-3
    print(l)
    if l==4:
        s=s[:i+2]+"-"+s[i+2:]
    return s


if __name__=="__main__":
    s=input()
    print(function(s))