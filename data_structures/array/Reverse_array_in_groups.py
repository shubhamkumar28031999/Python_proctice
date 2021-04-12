# def group_reverse(arr, x):
#     arr_2 = []
#     val_of_i = 0
#     if len(arr)>x:
#         for i in range(int(len(arr) / x)):
#             temp = arr[i * x:(i + 1) * x]
#             arr_2.extend(temp[::-1])
#             val_of_i = i
#         # print(arr_2)
#         if ((val_of_i) * x) <= len(arr):
#             # print(f"value of i {x * val_of_i}")
#             temp = arr[(val_of_i + 1) * x:]
#             # print(f"temp {temp}")
#             arr_2.extend(temp[::-1])
#     else:
#         arr_2=arr[::-1]
#     for val in arr_2:
#         print(val, end=" ")
#
#
# if __name__ == "__main__":
#     t = int(input())
#     for i in range(t):
#         n, x = list(map(int, input().strip().split()))
#         arr = list(map(int, input().strip().split()))
#         group_reverse(arr, x)
arr=[3,2,6,54]
arr.sort()
print(arr)