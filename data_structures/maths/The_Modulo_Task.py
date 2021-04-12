# Ishaan has been given a task by his teacher. He is given an integer N and asked to find some integer K for which N%K is the largest ( 1 <= K < N), where % stands for modulo.Ishaan has to complete this task as soon as possible, so help him do this.
#
# Input :
# The first line of input contains a single integer T denoting the number of test cases.Each test case contains an integer N.
#
# Output :
# For each test case, print the required answer in a new line.
#
# Constraints :
# 1 <= T <= 200
# 2 <= N <= 10^12
#
# Example :
# Input :
# 3
# 7
# 8
# 6
# Output :
# 4
# 5
# 4
#
# Explanation :
# Case 1 :
# 7%1 = 0
# 7%2 = 1
# 7%3 = 1
# 7%4 = 3
# 7%5 = 2
# 7%6 = 1
#
# Case 2 :
# 8%1 = 0
# 8%2 = 0
# 8%3 = 2
# 8%4 = 0
# 8%5 = 3
# 8%6 = 2
# 8%7 = 1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        num = int(input())

        print((num // 2) + 1)

# 2
# 675031245393
# 703531720457