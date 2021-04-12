def findPeakUtil(arr, low, high, n):
    mid = low + (high - low) / 2
    mid = int(mid)

    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
        (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid

    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)

    else:
        return findPeakUtil(arr, (mid + 1), high, n)

def findPeak(arr):
    n=len(arr)
    return findPeakUtil(arr, 0, n - 1, n)




if __name__=="__main__":
    arr = [1, 3, 20, 4, 1, 0, 100,10,4]
    print(findPeak(arr))