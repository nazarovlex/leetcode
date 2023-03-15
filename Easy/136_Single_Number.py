class Solution(object):
    def singleNumber(self, nums):
        nums = sorted(nums)
        while len(nums)>1:
            if nums[0] != nums[1]:
                return nums[0]
            elif nums[0] == nums[1]:
                nums.pop(0)
                nums.pop(0)

        return nums[0]




n = [1,1,2,3,2,4,5,4,5,6,7,6,7,6,7]
s = Solution()
result = s.singleNumber(nums=n)
print(result)
