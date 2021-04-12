def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i]=sorted(grid[i])
    flag=1

    for i in range(len(grid[0])):
        count=1
        for j in range(len(grid)-1):
            if grid[j][i]>grid[j+1][i]:
                count*=0
        flag*=count
    if flag == 1:
        return 'YES'
    else:
        return 'NO'

if __name__=="__main__":
    grid=[
        'ebacd',
        'fghij',
        'olmkn',
        'trpqs',
        'xywuv'
    ]
    print(gridChallenge(grid))
