from typing import List


class Solution:  # Binary search solution
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        if nums[right] > nums[0]:
            return nums[0]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


class Solution2:  # Easy python solution
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

nums = [3,4,5,1,2]
result = Solution().findMin(nums)
print(result)