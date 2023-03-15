class Solution(object):
    def removeElement(self, nums, val):
        c = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
                c += 1
        for i in range(c):
            nums.remove("_")

        # print(c, ", nums = ", nums)
        return c, nums


n = [3, 2, 2, 3]
v = 3
s = Solution()
result, nums = s.removeElement(n, v)
print(result, nums)
