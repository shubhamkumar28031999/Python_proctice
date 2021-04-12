from collections import Counter
arr=Counter(['aba','baba','aba','xzxb'])
print(arr['h'])




#
# if __name__=="__main__":
#     for _ in range(int(input())):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         temp_arr=[]
#         for i in range(n):
#             index=n-1
#             while index>=i and arr[index]%arr[i]!=0:
#                 index-=1
#             temp_arr.append(index+1)
#         print(temp_arr)