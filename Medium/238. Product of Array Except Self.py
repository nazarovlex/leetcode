from typing import List
import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        hash = {}

        for ind, num in enumerate(nums):
            if num not in hash:
                hash[num] = math.prod(nums[:ind] + nums[ind + 1:])
        for num in nums:
            answer.append(hash[num])
        return answer


nums = [1, 2, 3, 4]

result = Solution().productExceptSelf(nums)
print(result)
