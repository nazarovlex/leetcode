from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hash = {}
        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
        res = []
        for k, v in hash.items():
            if v == 1:
                res.append(k)
        return res


nums = [1, 2, 1, 3, 2, 5]
result = Solution().singleNumber(nums)
print(result)
