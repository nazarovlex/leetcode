from typing import List


# time: O(n*n) space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Solution with extra space but xn faster
# time: O(n) space: O(n)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for i in range(len(nums)):
            cnt = target - nums[i]
            if cnt in nums_dict.keys():
                return [i, nums_dict[cnt]]


nums = [2, 7, 11, 15]
target = 9
result = Solution().twoSum(nums, target)
print(result)
