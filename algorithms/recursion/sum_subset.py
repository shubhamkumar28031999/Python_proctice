def sum_subset(arr, l, r, sum=0):
    elements=[]
    if l > r:
        elements.append(sum)
        return elements
    elements.extend(sum_subset(arr, l + 1, r, sum))
    elements.extend(sum_subset(arr, l + 1, r, sum + arr[l]))
    return sorted(elements)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ele=sum_subset(arr,0,len(arr)-1)
        for val in ele:
            print(val,end=" ")
        print()