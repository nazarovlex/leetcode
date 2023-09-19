from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)

        res1 = nums1.intersection(nums2)
        res2 = nums1.intersection(nums3)
        res3 = nums2.intersection(nums3)

        res = res1.union(res2.union(res3))

        return [x for x in res]


nums1 = [1, 1, 3, 2]
nums2 = [2, 3]
nums3 = [3]
result = Solution().twoOutOfThree(nums1, nums2, nums3)
print(result)
