# from itertools import combinations
#
# def subArrayLength(l,r,arr):
#     l1=0
#     for i in range(l-1,r):
#         for j in range(i+1,r+1):
#             # if l<=max(arr[i:j])<=r:
#             l1+=len(arr[i:j])
#     print(l1)
#
#
#
#
#
# if __name__=="__main__":
#     n, m = map(int, input().split())
#     arr = list(map(int, input().split()))
#     for _ in range(m):
#         l, r = map(int, input().split())
#         subArrayLength(l,r,arr)
#
# n,m=map(int, input().split())
# arr=list(map(int, input().split()))
# for _ in range(m):
#     l,r=map(int, input().split())
#     l1=0
#     for i in range(0,n+1):
#         for j in range(i+1,n+1):
#             if l<=max(arr[i:j])<=r:
#                 print(arr[i:j])
#                 l1+=len(arr[i:j])
#     print(l1)


#
# from itertools import permutations
#
# def gen_all_substrings(s):
#     lt = lambda pair: pair[0] < pair[1]
#     index_pairs = filter(lt, permutations(range(len(s)+1), 2))
#     return (s[i:j] for i,j in index_pairs)
#
# def get_all_substrings(s):
#     print(list(gen_all_substrings(s)))
#
# arr=[1,2,3]
# get_all_substrings(arr)


# from itertools import permutations

# def genrate_all_substring(s):
#     lt= lambda pair: pair[0]<pair[1]
#     index_pairs=filter(lt,permutations(range(len(s)+1),2))
#     dp=dict()
#     for i,j in index_pairs:
#         if max(s[i:j]) not in dp:
#             dp[max(s[i:j])]=len(s[i:j])
#         else:
#             dp[max(s[i:j])] += len(s[i:j])
#     print(dp)
#     return dp
#
# n,m=map(int,input().split())
# arr=list(map(int,input().split()))
# dp=genrate_all_substring(arr)
# for _ in range(m):
#     l1=0
#     l,r=map(int,input().split())
#     for sub_string in dp:
#         if l<= max(sub_string)<=r:
#             l1+=len(sub_string)
#     print(l1)


from itertools import permutations

#
# def genrate_all_substring(s):
#     lt = lambda pair: pair[0] < pair[1]
#     index_pairs = filter(lt, permutations(range(len(s) + 1), 2))
#     dp = dict()
#     for i, j in index_pairs:
#         if max(s[i:j]) not in dp:
#             dp[max(s[i:j])] = len(s[i:j])
#         else:
#             dp[max(s[i:j])] += len(s[i:j])
#     print(dp)
#     return dp


def genrate_all_substring(s):
    lt= lambda pair: pair[0]<pair[1]
    index_pairs=filter(lt,permutations(range(len(s)+1),2))
    dp=dict()
    for i,j in index_pairs:
        if max(s[i:j]) not in dp:
                dp[max(s[i:j])]=len(s[i:j])
        else:
                dp[max(s[i:j])]+=len(s[i:j])
    return dp

n,m=map(int,input().split())
arr=list(map(int,input().split()))
dp=genrate_all_substring(arr)
for _ in range(m):
    l1=0
    l,r=map(int,input().split())
    for i in range(l,r+1):
        l1+=dp[i]
    print(l1)
