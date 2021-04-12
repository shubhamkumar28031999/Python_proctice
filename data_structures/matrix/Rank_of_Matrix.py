if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        matrix = []
        for i in range(3):
            temp = []
            for j in range(3):
                val1, val2, val3 = list(map(int,input().strip().split()))
                temp.append(val1)
                temp.append(val2)
                temp.append(val3)
            matrix.append(temp)
        for i in range(2):
            if matrix[i][0] != 0:
                first_element=matrix[i][0]
            else:
                if matrix[i][1] != 0:
                    first_element = matrix[i][1]
                else:
                    first_element = matrix[i][2]
            for j in range(i+1,3):
                multiply_val=