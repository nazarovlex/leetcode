from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1) & set(nums2)
        nums2 = []
        for num in nums1:
            nums2.append(num)
        return nums2


testcase_1 = [[1, 2, 2, 1], [4, 9, 5]]
testcase_2 = [[2, 2], [9, 4, 9, 8, 4]]

for i in range(len(testcase_1)):
    result = Solution().intersection(testcase_1[i], testcase_2[i])
    print(result)
