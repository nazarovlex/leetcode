from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_3 = nums[i] + nums[left] + nums[right]
                if sum_3 > 0:
                    right -= 1
                elif sum_3 < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1
        return res


nums = [-1, 0, 1, 2, -1, -4]
result = Solution().threeSum(nums)
print(result)
