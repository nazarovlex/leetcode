from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            c = 0
            for j in nums[:i] + nums[i + 1:]:
                if nums[i] > j:
                    c += 1
            res.append(c)

        return res


nums = [8, 1, 2, 2, 3]
result = Solution().smallerNumbersThanCurrent(nums)
print(result)
