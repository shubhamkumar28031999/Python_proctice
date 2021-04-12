# Python3 implementation to find the
# minimum of the maximum difference
# of the adjacent elements after
# removing K elements from the array
import sys

INT_MAX = sys.maxsize;
INT_MIN = -(sys.maxsize - 1);

print(INT_MAX)
print(INT_MIN)
# Function to find the minimum
# of the maximum difference of the
# adjacent elements after removing
# K elements from the array
def minimumAdjacentDifference(a, n, k):
    # Intialising the
    # minimum difference
    minDiff = INT_MAX;

    # Iterating over all
    # subarrays of size n-k
    for i in range(k + 1):

        # Maximum difference after
        # removing elements
        maxDiff = INT_MIN;
        for j in range(n - k - 1):
            for p in range(i, i + j + 1):
                maxDiff = max(maxDiff, a[p + 1] - a[p]);

                # Minimum Adjacent Difference
        minDiff = min(minDiff, maxDiff);

    return minDiff;


# Driver Code
if __name__ == "__main__":
    n = 5;
    k = 1;

    a = [3, 7, 8, 10, 14];

    print(minimumAdjacentDifference(a, n, k));