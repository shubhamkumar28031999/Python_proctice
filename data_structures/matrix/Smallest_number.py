from collections import deque
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        sum_of_digit, no_of_digit = list(map(int, input().strip().split()))
        stack=deque()
        if sum_of_digit>9*no_of_digit:
            print(-1)
        else:
            for j in range(no_of_digit):
                if sum_of_digit<=9:
                    stack.appendleft(sum_of_digit)
                    sum_of_digit=0
                if sum_of_digit>9:
                    sum_of_digit-=9
                    stack.appendleft(9)
            if stack[0]==0:
                k=0
                while stack[k]==0:
                    k+=1
                stack[k]-=1
                stack[0]=1

            for val in stack:
                print(val,end="")
            print()