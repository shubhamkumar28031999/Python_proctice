# name=input("").upper()
# no=int(input(""))
# x1=[]
# for i in range(0,no):
#     x1.append(int(input("")))
# a=[]
# word_count={char:name.count(char) for char in name}
# for x,y in word_count.items():
#     for j in range(0,y):
#         sum=0
#         for k in range(0,j+1):
#             sum+=ord(x)-64
#         a.append(sum)
#
# for z in x1:
#     if z in a:
#         print("Yes")
#     else:
#         print("No")
def weightedUniformStrings(s, queries):
    t=s[0]
    acc=-(ord(t) - 96)
    tot={}
    for i in s:
        if i ==t:
            acc+=ord(i) - 96
            tot[ord(i) - 96+acc if i != 0 else ord(i) - 96]=0
        else:
            acc=0
            tot[ord(i) - 96+acc]=0
        t=i
    return ['Yes' if i in tot else 'No' for i in queries]

