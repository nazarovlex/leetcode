from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [x * x for x in nums]
        return sorted(nums)


nums = [-4, -1, 0, 3, 10]
result = Solution().sortedSquares(nums)
print(result)
