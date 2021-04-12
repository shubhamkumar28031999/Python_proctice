
for _ in range(int(input())):
    c=bin(int(input()))[2:]
    A=""
    B=""
    flag=1
    for i in range(len(c)):
        if c[i]=="0":
            A+="1"
            B+="1"
        else:
            if flag==1:
                A+="1"
                B+="0"
                flag=0
            else:
                A+="0"
                B+="1"


    print(int(A,2)*int(B,2))