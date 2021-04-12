if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        final_x, final_y = list(map(int, input().strip().split()))
        paths = int(input())
        l1 = list(map(int, input().strip().split()))
        minx = 0
        miny = 0
        for j in range(0, paths*2, 2):
            minx += l1[j]
            miny += l1[j + 1]

        x = final_x - minx
        y = final_y - miny

        print(x, end=" ")
        print(y, end=" ")
        print()
#
# 1
# 10 7
# 10
# 4 5 2 6 2 5 6 7 7 5 4 4 7 8 9 7 5 8 4 10