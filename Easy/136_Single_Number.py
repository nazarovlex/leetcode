class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for num in n:
            res = res ^ num
        return res



n = [1,1,2,3,2,4,5,4,5,6,7,6,7,6,7]
s = Solution()
result = s.singleNumber(nums=n)
print(result)
