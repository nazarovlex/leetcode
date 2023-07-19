from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        res1 = []
        res2 = []
        for num in nums1:
            if num not in nums2:
                res1.append(num)
        for num in nums2:
            if num not in nums1:
                res2.append(num)

        return [res1, res2]


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = Solution().findDifference(nums1, nums2)
print(result)
