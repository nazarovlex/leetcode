class Solution(object):
    def majorityElement(self, nums):
        l = len(nums) / 2
        set_nums = set(nums)
        for num in set_nums:
            if nums.count(num) > l:
                return int(num)


n = [2, 2, 1, 1, 1, 2, 2]
result = Solution().majorityElement(n)
print(result)
