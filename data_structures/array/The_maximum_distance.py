# if __name__=="__main__":
#     n=int(input())
#     arr=list(map(int,input().strip().split()))
#     for _ in range(int(input())):
#         query=list(map(int,input().strip().split()))
#         if query[0]==1:
#             for i in range(query[1]-1,query[2]):
#                 arr[i]+=query[3]
#
#             # print(arr)
#         if query[0] == 2:
#             for i in range(query[1]-1, query[2]):
#                 arr[i] *= query[3]
#             # print(arr)
#         if query[0] == 3:
#             mini=-1
#             try:
#                 mini=arr.index(query[1])
#             except:
#                 pass
#             if mini==-1:
#                 print(mini)
#             else:
#                 maxi=arr.index(query[1],n-1,mini)
#                 print(maxi-mini+1)
