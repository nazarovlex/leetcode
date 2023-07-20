from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(sum(nums[:i+1]))
        return res



nums = [1,2,3,4]
result = Solution().runningSum(nums)
print(result)
