# def TOH(num, tow1, tow2, tow3):
#     sum=0
#     if num > 0:
#         sum=TOH(num - 1, tow1, tow3, tow2) +sum+1
#         print("move disk " + str(num) + " from rod " + str(tow1) + " to rod " + str(tow3))
#         sum=TOH(num - 1, tow2, tow1, tow3) +sum
#     return sum
#
# if __name__ == "__main__":
#     t = int(input())
#     for i in range(t):
#         num = int(input())
#         sum1=TOH(num, 1, 2, 3)
#         print(sum1)

def TOH(num, tow1, tow2, tow3,moves):
    sum=0
    if num > 0:
        sum=TOH(num - 1, tow1, tow3, tow2,moves) +sum+1
        if sum == moves:
            print(str(tow1) + " " + str(tow3))
            return
        sum=TOH(num - 1, tow2, tow1, tow3,moves) +sum
    return sum

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        num,moves = list(map(int, input().strip().split()))
        TOH(num, 1, 2, 3,moves)
