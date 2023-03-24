from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        for _ in range(2):
            nums.remove(max(nums))
        return max(nums)


testcase = [[3, 2, 1], [1, 2], [2, 2, 3, 1]]
for test in testcase:
    result = Solution().thirdMax(test)
    print(result)
