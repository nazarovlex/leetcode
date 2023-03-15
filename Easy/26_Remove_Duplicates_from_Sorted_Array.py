class Solution(object):
    def removeDuplicates(self, nums):
        nums = sorted(set(nums))
        return nums


n = [0,0,1,1,1,2,2,3,3,4]

s = Solution()
result = s.removeDuplicates(n)
print(result)
