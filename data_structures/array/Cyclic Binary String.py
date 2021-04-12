import math
def maximumPower(s):
    l=len(s)
    max_pow=0
    max_num=0
    for _ in range(l):
        num=int(s,2)
        max_pow=max(max_pow,int(math.log((num & (~(num - 1))),2)))
        s=s+s[0]
        s=s[1:]
    return max_pow


if __name__ == '__main__':


    s = input()

    result = maximumPower(s)

    print(result)
