# def coin_change(total,coins):
#     dp=[0 for _ in range(total+1)]
#     for i in range(len(coins)):
#         for j in range(coins[i],total+1):
#             if j%coins[i]==0:
#                 dp[j]=j//coins[i]
#             else:
#                 dp[j]=min(dp[j],1+dp[j-coins[i]])
#     print(dp)
#
#
#
# if __name__=="__main__":
#     n=int(input())
#     coins=[1,2,5]
#     coin_change(n,coins)
 


if __name__=="__main__":
    n=input()
    temp=[]
    for i in range(0,len(n),2):
        temp.append(n[i])
    print(int("".join(temp)))