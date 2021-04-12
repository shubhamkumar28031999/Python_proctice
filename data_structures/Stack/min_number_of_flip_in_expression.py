def sol(exp):
    l=len(exp)
    if l%2!=0:
        return "Invalid Expreseeion"
    else:
        forword=0
        backword=0
        for i in range(l):
            if exp[i]=='(':
                forword+=1
            else:
                backword+=1
        return abs(backword-forword)//2


exp='))(())'
print(sol(exp))