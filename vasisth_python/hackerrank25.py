from collections import Counter

no = int(input(""))
income = 0
size = list(Counter(list(map(int, input("").split(" ")))).items())
size1=[]
for i in size:
    size1.append(list(i))

customer = int(input(""))
size_price_list = []
for i in range(customer):
    size_price = list(map(int, input("").split(" ")))
    size_price_list.append(size_price)
for i in size_price_list:
    for j in size1:
        if j[0] == i[0]:
            if j[1] > 0:
                j[1] = j[1] - 1
                income = income + i[1]
            else:
                pass
        else:
            pass
print(income)
