def isInterleave(A, B, C):
    if len(A) == len(C) == len(B) == 0:
        return True

    else:
        return ((len(A) > 0 and len(C) > 0) and A[0] == C[0] and isInterleave(A[1:], B, C[1:])) or \
               ((len(B) > 0 and len(C) > 0) and B[0] == C[0] and isInterleave(A, B[1:], C[1:]))




if __name__ =="__main__":
    t= int(input())
    for i in range(t):
        arr= input().strip().split()
        if isInterleave(arr[0], arr[1], arr[2]):
            print(1)
        else:
            print(0)


# list1=['xy','y']
# val='z'
# if val in list1:
#     print(1)
# else:
#     print(2)