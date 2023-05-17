from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        nums.sort()

        last, max_len = 0, 0
        res = set()

        for num in nums:
            if len(res) == 0:
                res.add(num)

            elif abs(last - num) == 1:
                res.add(num)

            elif last == num:
                continue

            elif abs(last - num) > 1:
                max_len = max(max_len, len(res))
                res = set()
                res.add(num)

            last = num

        max_len = max(max_len, len(res))
        return max_len


nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
result = Solution().longestConsecutive(nums)
print(result)
