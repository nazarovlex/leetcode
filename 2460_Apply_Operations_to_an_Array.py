class Solution(object):
    def applyOperations(self, nums):
        i = 0
        while i< len(nums)-1:
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                i += 2
                continue
            i += 1
        zero = nums.count(0)
        for i in range(zero):
            nums.remove(0)
            nums.append(0)
        return nums

n = [1, 2, 2, 1, 1, 0]
s = Solution()
result = s.applyOperations(n)
print(result)
