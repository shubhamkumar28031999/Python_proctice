# import math
#
# if __name__ == "__main__":
#     t = int(input())
#     dp = dict()
#
#     for i in range(t):
#         num = int(input())
#         sum = 0
#         for j in range(1, num + 1):
#             under_root5 = round(math.sqrt(5), 10)
#             left = round(((1 + under_root5) / 2) ** j, 10)
#             right = round(((1 - under_root5) / 2) ** j, 10)
#             val = (left - right) / under_root5
#             if int(val) % 2 == 0:
#                 sum += val
#             else:
#                 pass
#         print(int(sum))

def fabonachi(num, dp):
    if num in dp:
        return dp[num]
    else:
        if num == 0:
            dp[0] = 0
            return 0
        if num == 1:
            dp[1] = 0
            return 1
        else:
            val = fabonachi(num - 1, dp) + fabonachi(num - 2, dp)
            dp[num] = val
            return val


if __name__ == "__main__":
    t = int(input())
    dp = dict()

    for i in range(t):
        num = int(input())
        sum=0
        for j in range(1, num + 1):
            if j in dp:
                if dp[j]%2==0:
                    sum+=dp[j]
                else:
                    pass
            else:
                val = fabonachi(j, dp)
                dp[j] = val
                if dp[j]%2==0:
                    sum+=dp[j]
                else:
                    pass

        print(sum)