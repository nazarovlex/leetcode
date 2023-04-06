from typing import List


class Solution:  # time:O(n*n) space: O(1)
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                if height[i] > height[j]:
                    res = max(res, height[j] * (j - i))
                else:
                    res = max(res, height[i] * (j - i))
        return res


class Solution2:  # time:O(n) space: O(1)
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            if height[left] > height[right]:
                res = max(res, height[right] * (right - left))
                right -= 1
            else:
                res = max(res, height[left] * (right - left))
                left += 1
        return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = Solution2().maxArea(height)
print(result)
