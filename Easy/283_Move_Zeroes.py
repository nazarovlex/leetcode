class Solution(object):
    def moveZeroes(self, nums):
        zero = nums.count(0)
        for i in range(zero):
            nums.remove(0)
        for i in range(zero):
            nums.append(0)


nums = [0, 1, 0, 0, 0, 0, 3, 12]
s = Solution()
s.moveZeroes(nums)
print(nums)
