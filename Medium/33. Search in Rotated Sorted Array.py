from typing import List


class Solution:  # Fast python solution
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1


class Solution2:  # Real solution
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if target < nums[0] < nums[mid]:
                left = mid + 1
            elif target >= nums[0] > nums[mid]:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = Solution().search(nums, target)
print(result)
