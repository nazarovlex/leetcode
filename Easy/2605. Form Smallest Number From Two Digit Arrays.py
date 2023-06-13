from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if set(nums1) & set(nums2):
            return int(min(set(nums1) & set(nums2)))
        return int(str(min(min(nums1), min(nums2))) + str(max(min(nums1), min(nums2))))


nums1 = [3, 5, 2, 6]
nums2 = [3, 1, 7]
result = Solution().minNumber(nums1, nums2)
print(result)
