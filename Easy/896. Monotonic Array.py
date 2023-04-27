from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sort_nums = sorted(nums)
        return True if nums == sort_nums or nums == sort_nums[::-1] else False


nums = [6, 5, 4, 4]
result = Solution().isMonotonic(nums)
print(result)
