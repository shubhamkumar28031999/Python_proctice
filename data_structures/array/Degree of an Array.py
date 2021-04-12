import collections
import sys


class Solution:
    def frequency(self, arr):
        return dict(collections.Counter(arr))

    def findShortestSubArray(self, arr):
        l = len(arr)
        freq = self.frequency(arr)
        max_frequency = max(freq.values())
        min_length = sys.maxsize
        for key, val in freq.items():
            if val == max_frequency:
                index_left = arr.index(key)
                right_index = l - 1 - arr[::-1].index(key)
                min_length = min(min_length, right_index - index_left + 1)
        return min_length


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 1]
    solution = Solution()
    print(solution.findShortestSubArray(arr))
