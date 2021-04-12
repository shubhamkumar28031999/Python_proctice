#
# if __name__=="__main__":
#     t=int(input())
#     for i in range(t):
#         n=int(input())
#         for j in range(n):
#             s=input()
#             if j==0 or j==n-1:
#                 print(s)
#             else:
#                 s=[str(d) for d in s]
#                 for k in range(len(s)):
#                     if k==0 or k==len(s)-1:
#                         pass
#                     else:
#                         s[k]='$'
#                 for val in s:
#                     print(val,end="")
#                 print()


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        s = 65
        for j in range(n):

            if j == 0 or j == n - 1:
                count = 0
                while count < n:
                    print(chr(s), end="")
                    count += 1
                    int(s)
                    s += 1
            else:
                count = 0
                while count < n:
                    if count == 0 or count == n - 1:
                        print(chr(s), end="")
                        count += 1
                        int(s)
                        s += 1
                    else:
                        print("$", end="")
                        count+=1
            print()