class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
            elif i == len(nums) - 1:
                return i + 1


nums = [1, 3, 5, 6]
target = 7
s = Solution()
ret = s.searchInsert(nums=nums, target=target)
print(ret)
