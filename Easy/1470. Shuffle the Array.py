from typing import List, Optional


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        l, r = 0, n
        while r < len(nums):
            res.append(nums[l])
            res.append(nums[r])
            l += 1
            r += 1
        return res


nums = [2, 5, 1, 3, 4, 7]
n = 3
result = Solution().shuffle(nums, n)
print(result)
