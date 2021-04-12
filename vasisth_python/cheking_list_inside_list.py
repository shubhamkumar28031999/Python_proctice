li=[1,2,3,4,[3,4],[4,5,6]]
count=0
for i in li:
    if type(i) == list:
        count+=1
print(count)