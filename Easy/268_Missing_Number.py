class Solution(object):
    def missingNumber(self, nums):
        for i in range(0, len(nums) + 1):
            if i not in nums:
                return i

    def missingNumber2(self, nums):
        nums = sorted(nums)
        full_nums = [i for i in range(len(nums) + 1)]
        res = [x for x in full_nums + nums if x not in nums]
        return res[0]

n = [3, 0, 1]
s = Solution()
result = s.missingNumber(nums=n)
print(result)

s = Solution()
result = s.missingNumber2(nums=n)
print(result)



