# import math
# route=['TH','GA','IC','HA','TE','LU','NI','CA']
# distance=[800,600,750,900,1400,1200,1100,1500]
# n1=input().upper()
# n2=input().upper()
# if n1==n2:
#     print('INVALID INPUT')
# else:
#     k=[]
#     for r in range(len(route)):
#         if route[r] in [n1,n2]:
#             k.append(r)
#     total_dis=sum(distance[k[0]:k[1]+1])
#     print(f"{float(math.ceil(total_dis/1000*5))} INR")

#
# sum1 = 0
# sum2 = 0
# n1 = int(input())
# n2 = int(input())
# for _ in range(n1):
#     s = float(input())
#     sum1 = sum1 + s
#
# t1 = sum1 * 18
# for _ in range(n2):
#     s2 = float(input())
#     sum2 = sum2 + s2
# t2 = sum2 * 12
# print(t1 + t2)

# if __name__=="__main__":
#     n=int(input())
#     m=int(input())
#     p=int(input())
#     k = int(input())
#     j = int(input())
#     if m==0 or p==0:
#         print("input error")
#     else:
#
#         print(n-k//m-j//p)
#
# character=input()
# num=int(input())
# gener={'c':{1:'Espresso coffee',
#             2:'Cappuccino Coffee',
#             3:'Latte Coffee'},
#        't':{1:'Plain Tea',
#             2:'Assam Tea',
#             3:'Ginger tea',
#             4:'Cardamon Tea',
#             5:'Masala Tea',
#             6:'Leamon Tea',
#             7:'Green Tea',
#             8:'Organic Darjeeling Tea'
#     },
#        's':{
#             1:'Hot and Sour Soup',
#             2:'Veg Corn Soup',
#             3:'Tomato Soup',
#             4:'Spicy Tomato Soup',
# },
#        'b':{
#                 1:'Hot Chocolate Drink',
#                 2:'Badam Drink',
#                 3:'Badam-Pista Drink'
#         }
# }
#
#
#
#
# if character in gener:
#     if num in gener[character]:
#         print('Welcome to CCD!')
#         print(gener[character][num])
#     else:
#         print('INVALID OPTION')
# else:
#     print('INVALID OPTION')
# import re
#
# def atoi(text):
#     return int(text) if text.isdigit() else text
#
# def natural_keys(text):
#     return [ atoi(c) for c in re.split(r'(\d+)', text) ]
#
# M=10
# N=5
import sys
# if __name__=="__main__":
#     for _ in range(int(input())):
#         l=int(input())
#         arr=list(map(int,input().split()))
#         su=max(arr)
#         su2=0
#         for x in range(0,l,2):
#             su2+=arr[x]
#         su=max(su,su2)
#         su2=0
#         for x in range(1,l,2):
#             su2+=arr[x]
#         su = max(su, su2)
#         print(su)
# def combinations(iterable, r):
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield tuple(pool[i] for i in indices)
#
#
# if __name__=="__main__":
#     for _ in range(int(input())):
#         num_laddo,kids=map(int,input().split())
#         arr=list(map(int,input().split()))
#         arr.sort()
#         s=sys.maxsize
#         for i in range(0,num_laddo-kids):
#             temp=arr[i:i+kids+1]
#             print(temp)
#             s=min(s,temp[-1]-temp[0])
#         print(s)

#
# y=(((3/4)/2)*(2/31)-(5/7)/((8/3)*(73/10)))*((16/5)*(9/2)*(16/3))
# print(y)
#
# if __name__=="__main__":
#     d={
#         1:["Malaysia",0],
#         2: ["Australia", 0],
#         3: ["Germany", 0],
#         4: ["Dubai", 0],
#         5: ["France", 0]
#     }
#     m=0
#     for _ in range(25):
#         val=int(input())
#         if 0<val<6:
#             d[val][1]+=1
#             m=max(m,d[val][1])
#         else:
#             print("Invalid Input")
#             break
#     for x,y in d.items():
#         if y[1]==m:
#             print(y[0])

for _ in range(int(input())):
    s=input()
    l=len(s)
    s=s.replace('*','')
    ind=s.index('M')
    if s[0]=='M':
        if s[1]=='G':
            print("YES")
        else:
            print("No")
    elif s[l-1]=='M':
        if s[l-2]=='G':
            print("YES")
        else:
            print("No")

    else:
        if s[ind-1]=='T' or s[ind+1]=='T':
            print("NO")
        else:
            print("YES")
