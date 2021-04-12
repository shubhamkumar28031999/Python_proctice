def solve(arr1,arr2):
    temp_arr1=sorted(arr1)
    temp_arr2=sorted(arr2)
    temp_dict1={}
    temp_dict2={}
    l=len(arr1)
    for i in range(l):
        temp_dict1[arr1[i]]=i
    for i in range(l):
        temp_dict2[arr2[i]]=i
    ans=-10**9
    low=0
    high=l-1
    while low<high:
        temp1=temp_arr1[high]-temp_arr1[low]
        temp2=abs(arr2[temp_dict1[temp_arr1[high]]]-arr2[temp_dict1[temp_arr1[low]]])
        ans=max(ans,temp2+temp1)
        low+=1
        high-=1
    low=0
    high=l-1
    while low<high:
        temp1=temp_arr2[high]-temp_arr2[low]
        temp2=abs(arr1[temp_dict2[temp_arr2[high]]]-arr1[temp_dict2[temp_arr2[low]]])
        ans=max(ans,temp2+temp1)
        low+=1
        high-=1
    return ans


arr1=[4,5,1,2,3]
arr2=[1,2,7,4,6]
print(solve(arr1,arr2))