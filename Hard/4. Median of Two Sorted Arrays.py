from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = sorted(nums1 + nums2)
        if len(nums1) % 2 > 0:
            return nums1[len(nums1) // 2]
        else:
            return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2


n1 = [1, 3]
n2 = [2, 7]
result = Solution().findMedianSortedArrays(n1, n2)
print(result)
