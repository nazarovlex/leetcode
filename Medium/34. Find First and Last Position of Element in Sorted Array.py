from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        try:
            res.append(nums.index(target))
            res.append(len(nums) - 1 - nums[::-1].index(target))
        except ValueError:
            return [-1, -1]
        return res


nums = [5, 7, 7, 8, 8, 10]
target = 8
result = Solution().searchRange(nums, target)
print(result)
