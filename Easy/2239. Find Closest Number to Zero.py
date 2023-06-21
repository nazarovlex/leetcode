class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        min_num = nums[0]
        for num in nums[1:]:
            if abs(num) < abs(min_num):
                min_num = num
            elif abs(min_num) == abs(num) and num > min_num:
                min_num = num
        return min_num


nums = [-4, -2, 1, 4, 8]
result = Solution().findClosestNumber(nums)
print(result)
