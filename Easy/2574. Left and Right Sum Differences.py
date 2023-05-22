from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(abs(sum(nums[:i]) - sum(nums[i + 1:])))
        return res


n = [10, 4, 8, 3]
result = Solution().leftRightDifference(n)
print(result)
