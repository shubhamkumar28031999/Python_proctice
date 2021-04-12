def bin_search(A, left, right, k):

    if right >= left:
        mid = (left + right) // 2
        if A[mid] == k:
            return mid
        if A[mid] > k:
            return bin_search(A[:mid], left, mid - 1, k)
        else:

            return bin_search(A[mid + 1:], mid + 1, right, k)
    else:
        return -1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        group_reverse(arr, x)