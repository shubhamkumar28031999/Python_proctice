import statistics
def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    return statistics.median(nums1)


if __name__=="__main__":
    nums1 = [1, 3]
    nums2 = [2,7]
    print(findMedianSortedArrays(nums1,nums2))