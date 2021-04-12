# def minDist():
#     arr = [1,2,3,4,5,6,7,8]
#     n=8
#     x=3
#     y=6
#     if x in arr and y in arr:
#         x_index = []
#         y_index = []
#         diff = []
#         for i in range(n):
#             if arr[i] == x:
#                 x_index.append(i)
#             else:
#                 pass
#         for i in range(n):
#             if arr[i] == y:
#                 y_index.append(i)
#             else:
#                 pass
#         print(x_index)
#         print(y_index)
#         for x_in in x_index:
#             for y_in in y_index:
#                 print(x_in)
#                 print(y_in)
#                 diff.append(abs(x_in - y_in))
#
#         return min(diff)
#
#     else:
#         return -1
#
#
# if __name__=="__main__":
#     # t = int(input())
#     # for i in range(t):
#     #     n = int(input())
#     #     arr=list(map(int,input().strip().split()))
#     #     x,y=list(map(int,input().strip().split()))
#     print(minDist())

arr= [1,2,3,4,5]
arr.remove(2)
print((arr))