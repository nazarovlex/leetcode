class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t + 1*t

result = Solution().theMaximumAchievableX(5,4)
print(result)