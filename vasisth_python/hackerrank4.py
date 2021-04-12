lst = list(map(int,input().strip().split(' ')))
x = sum(lst)
print(f"{x-max(lst)} {x-min(lst)}")

