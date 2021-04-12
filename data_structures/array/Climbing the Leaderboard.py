def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked))
    arr = []
    l=len(ranked)
    index=0
    for val in player:
        while index<l and val>=ranked[index]:
            index+=1

        arr.append(l-index+1)
    print(arr)


if __name__ == "__main__":
    ranked = [100, 90, 90, 80, 75, 60]
    player = [50, 65, 77, 90, 102]
    climbingLeaderboard(ranked, player)
