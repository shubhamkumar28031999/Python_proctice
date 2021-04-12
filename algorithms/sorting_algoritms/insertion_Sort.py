
import os

def insertionSort1(n, arr):
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    if n <= 1:
        return
    insertionSort1(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while (j >= 0 and arr[j] > last):
        arr[j + 1] = arr[j]
        fptr.write(' '.join(arr))
        fptr.write('\n')
        j = j - 1
        print()
    arr[j + 1] = last


def display(arr):
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(' '.join(arr))
    fptr.write('\n')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
    display(arr)
