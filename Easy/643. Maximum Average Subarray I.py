from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = min(nums)
        if len(nums) == k:
            return sum(nums) / k
        cnt = 0
        substring = 0
        index = 0
        for num in nums:
            if cnt < k:
                substring += num
                cnt += 1
            if cnt == k:
                cnt -= 1
                max_avg = max(max_avg, substring / k)
                substring -= nums[index]
                index += 1

        return max_avg


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 5
result = Solution().findMaxAverage(nums, k)
print(result)
