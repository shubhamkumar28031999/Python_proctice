def longestSubstringWithoutRepeting(s):
    arr=[-1]*256
    n=len(s)
    i=0
    max_len=0
    for end in range(n):
        i=max(i,arr[ord(s[end])]+1)
        max_len=max(max_len,end-i+1)
        arr[ord(s[end])]=end
    return max_len
if __name__=="__main__":
    s='tmmzuxt'
    print(longestSubstringWithoutRepeting(s))
