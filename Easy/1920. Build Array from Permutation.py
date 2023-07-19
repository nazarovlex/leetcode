from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[x] for x in nums]


nums = [0, 2, 1, 5, 3, 4]
result = Solution().buildArray(nums)
print(result)
