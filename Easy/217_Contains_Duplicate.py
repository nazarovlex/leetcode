class Solution(object):
    def containsDuplicate(self, nums):
        s = set(nums)
        if len(s)==len(nums):
            return False
        else:
            return True


n = [1,2,3,1]
result = Solution().containsDuplicate(n)
print(result)