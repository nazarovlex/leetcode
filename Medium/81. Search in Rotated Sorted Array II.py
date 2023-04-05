from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return True if nums[0] == target else False
        left, right = 0, len(nums) - 1
        nums.sort()
        if target == nums[0] or target == nums[-1]:
            return True
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return True
        return False


class Solution2:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] > nums[right]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

nums = [2,5,6,0,0,1,2]
target = 0
result = Solution().search(nums,target)
print(result)