import math
from collections import deque
def max_area_histogram(histogram):
    stack=deque()
    max_area=0
    index=0
    while index<len(histogram):
        if (not stack) or (histogram[stack[-1]]<=histogram[index]):
            stack.append(index)
            index+=1
        else:
            top_of_stack=stack.pop()
            area=(histogram[top_of_stack] * ((index - stack[-1] - 1)  if stack else index))
            max_area = max(max_area, area)
    while stack:
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)
    return max_area

def horizontal_max_Area(Matrix,n,m):
    arr=[0 for x in range(m)]
    max_Area=0
    for i in range(n):
        for j in range(m):
            if Matrix[i][j]==0:
                arr[j]=0
            else:
                arr[j]+=1
        max_Area=max(max_Area,max_area_histogram(arr))
    return max_Area

def vartical_max_Area(Matrix,n,m):
    arr=[0 for x in range(n)]
    max_Area=0
    for i in range(m):
        for j in range(n):
            if Matrix[j][i]==0:
                arr[j]=0
            else:
                arr[j]+=1
        max_Area=max(max_Area,max_area_histogram(arr))
    return max_Area


def maxRectangle(M, n, m):
    return max(vartical_max_Area(M,n,m),horizontal_max_Area(M,n,m))






if __name__=="__main__":
    n = 4
    m = 4
    M = [[0,1,1,0],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,0,0]]
    print(maxRectangle(M,n,m))
