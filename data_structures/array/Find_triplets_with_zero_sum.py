# def findTripletsslow(arr):
#     found=0
#     for i in range(len(arr)-2):
#         for j in range(i+1,len(arr)-1):
#             for k in range(j+1,len(arr)):
#                 if arr[i]+arr[j]+arr[k]==0:
#                     found=1
#     return found
#
# def findTriplets(arr):
#     found=0
#     for i in range(len(arr)-2):
#         s = set()
#         for j in range(i+1,len(arr)-1):
#             if (arr[i]+arr[j])*-1 in s:
#                 found=1
#             else:
#                 s.add(arr[j])
#     return found
#
# if __name__ =="__main__":
#     t= int(input())
#     for i in range(t):
#         arr= list(map(int,input().strip().split()))
#         val = findTriplets(arr)
#         print(val)



# 4 -16 43 4 7 -36 18
# 4 -24 34 -35 60 -24 72 18 97 -54 12 -81 13 -43
# arr=[1,2,3,4,5]
# arr.remove(1)
# print(arr)
# li=[1,2,3,4,5]
# ls=[2,3,4]
# print()

