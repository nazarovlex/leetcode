class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    res += 1
        return res


nums = [1, 2, 3, 1, 1, 3]
result = Solution().numIdenticalPairs(nums)
print(result)
