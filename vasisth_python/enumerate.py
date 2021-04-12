names=['abc','shubham','kumar']
pos=0
for name in names:
    print(f"{pos}----->{name}")
    pos+=1

print("--------by enumarate function-------")
for pos,name in enumerate(names):
    print(f"{pos}----->{name}")

def find_pos(l,target):
    for pos,name in enumerate(l):
        if name==target:
            return pos
    return -1
print(find_pos(names,'shubham'))
