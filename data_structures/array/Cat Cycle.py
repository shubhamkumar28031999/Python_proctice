for _ in range(int(input())):
    n,k=map(int,input().split())
    position_A=n
    position_B=1
    # print(f"A={position_A}   B={position_B}")
    position_B=+(n//k)
        # print(f"A={position_A}   B={position_B}")


    print(position_B)