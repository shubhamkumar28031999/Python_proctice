# Siddhant made a special series and named it as G.F Series.The series follows this
# trend  Tn=(Tn-2)2-(Tn-1)  in which the first and the second term are 0 and 1 respectively.
# Help Siddhant to find  upto N terms of the series .
def series(num,dp):
    if num in dp:
        return dp[num]
    else:
        if num==1:
            dp[1] = 0
            return 0
        if num == 2:
            dp[2] = 1
            return 1
        else:
            val=series(num-2,dp)**2-series(num-1,dp)
            dp[num]=val
            return val


if __name__=="__main__":
    t= int(input())
    dp=dict()
    for i in range(t):
        num=int(input())
        for j in range(1,num+1):
            if j in dp:
                print(dp[j],end=" ")
            else:
                val=series(j,dp)
                print(val,end=" ")
        print()
