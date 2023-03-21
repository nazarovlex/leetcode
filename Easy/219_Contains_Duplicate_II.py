from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False

        for i in range(len(nums)):

            if nums[i + 1:].count(nums[i]) >= 1 and abs(i - nums.index(nums[i], i + 1)) <= k:
                return True
        return False


nums, k = [1, 2, 3, 1], 3
result = Solution().containsNearbyDuplicate(nums, k)
print(result)
