from typing import List
import math


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return nums[0]
        passed_nums = set()
        for num in nums:
            if num in passed_nums:
                return num
            else:
                passed_nums.add(num)


nums = [1, 3, 4, 2, 2]
result = Solution().findDuplicate(nums)
print(result)
