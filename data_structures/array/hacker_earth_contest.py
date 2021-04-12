
segment_tree = [0] * (4 * 1000000);
def build(A, start, end, node):
    if (start == end):
        segment_tree[node] = A[start];

    else:
        mid = (start + end) // 2;
        segment_tree[node] = max(
            build(A, start, mid, 2 * node + 1),
            build(A, mid + 1, end, 2 * node + 2));

    return segment_tree[node]


def query(start, end, l, r, node):
    if (start > r or end < l):
        return -1

    if (start >= l and end <= r):
        return segment_tree[node]

    mid = (start + end) // 2

    return max(query(start, mid, l,
                     r, 2 * node + 1),
               query(mid + 1, end, l,
                     r, 2 * node + 2))


def longestSubArray(A, N, K):
    res = 1
    preSum = [0] * (N + 1)
    preSum[0] = A[0]
    for i in range(N):
        preSum[i + 1] = preSum[i] + A[i]
    build(A, 0, N - 1, 0)
    for i in range(N):

        start = i
        end = N - 1
        max_index = i
        while start <= end:
            mid = (start + end) // 2
            max_element = query(0, N - 1, i, mid, 0)
            expected_sum = (mid - i + 1) * max_element;
            actual_sum = preSum[mid + 1] - preSum[i];
            if (expected_sum - actual_sum <= K):
                start = mid + 1;
                max_index = max(max_index, mid);
            else:
                end = mid - 1;
        res = max(res, max_index - i + 1);
    return res;

if __name__ == "__main__":
    arr = [2, 0, 4, 6, 7];
    K = 6;
    N = len(arr);

    print(longestSubArray(arr, N, K));