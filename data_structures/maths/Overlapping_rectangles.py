if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        flag = False
        rec1_x1, rec1_y1, rec1_x2, rec1_y2 = list(map(int, input().strip().split()))
        rec2_x1, rec2_y1, rec2_x2, rec2_y2 = list(map(int, input().strip().split()))
        if rec2_x1 in range(rec1_x1+1, rec1_x2):
            print("case 1")
            flag = True
        if rec2_x2 in range(rec1_x1+1, rec1_x2):
            print("case 2")
            flag = True
        if rec2_y1 in range(rec1_y1+1, rec1_y2):
            print("case 3")
            flag = True
        if rec2_y2 in range(rec1_y1+1, rec1_y2):
            print("case 4")
            flag = True


        if rec1_x1 in range(rec2_x1+1, rec2_x2):
            print("case 5")
            flag = True
        if rec1_x2 in range(rec2_x1+1, rec2_x2):
            print("case 6")
            flag = True
        if rec1_y1 in range(rec2_y1+1, rec2_y2):
            print("case 7")
            flag = True
        if rec1_y2 in range(rec2_y1+1, rec2_y2):
            print("case 8")
            flag = True
        if flag == True:
            print(1)

        else:
            print(0)
# 2
# 0 10 10 0
# 5 5 15 0
# 0 2 1 1
# -2 -3 0 2

#
# 1
# 22 21 28 92
# 96 73 44 82