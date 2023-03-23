from typing import List


class Solution(object):
    def moveZeroes(self, nums):
        zero = nums.count(0)
        for i in range(zero):
            nums.remove(0)
        for i in range(zero):
            nums.append(0)
        return nums


class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
        return nums


nums = [0, 1, 0, 0, 0, 0, 3, 12]
s = Solution()
s.moveZeroes(nums)
print(nums)
