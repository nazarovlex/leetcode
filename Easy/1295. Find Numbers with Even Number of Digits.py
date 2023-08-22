from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                cnt += 1
        return cnt


nums = [12, 345, 2, 6, 7896]
result = Solution().findNumbers(nums)
print(result)
