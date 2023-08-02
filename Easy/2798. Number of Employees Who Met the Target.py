from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        for ind, num in enumerate(hours):
            if num >= target:
                return len(hours[ind:])
        return 0


hours = [0, 1, 2, 3, 4]
target = 2
result = Solution().numberOfEmployeesWhoMetTarget(hours, target)
print(result)
