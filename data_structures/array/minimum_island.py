class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g
    def isSafe(self, i, j, visited):
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])
    def DFS(self, i, j, visited):
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

        visited[i][j] = True

        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)

    def countIslands(self):
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] == False and self.graph[i][j] ==1 :
                    self.DFS(i, j, visited)
                    count += 1
        return count


def numIslands(grid):
    countOfIsland = 0
    if len(grid) is 0:
        return 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] is "*":
                countOfIsland += 1
                dfs(row, col, grid, len(grid), len(grid[0]))
    return countOfIsland


def dfs(row, col, grid, rowlen, collen):
    if row < 0 or row >= rowlen or col < 0 or col >= collen or grid[row][col] is ".":
        return
    else:
        grid[row][col] = "."
        dfs(row - 1, col, grid, rowlen, collen)
        dfs(row, col - 1, grid, rowlen, collen)
        dfs(row + 1, col, grid, rowlen, collen)
        dfs(row, col + 1, grid, rowlen, collen)


for _ in range(int(input())):
    n,m=map(int,input().split())
    grid=[]
    for _ in range(n):
        grid.append(list(input()))

    # for i in range(n):
    #     for j in range(m):
    #         if grid[i][j]=='.':
    #             grid[i][j]=0
    #         else:
    #             grid[i][j]=1
    s=Graph(n,m,grid)
    print(s.countIslands())


