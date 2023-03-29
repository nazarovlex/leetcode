from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        for i in range(1, len(timeSeries)):
            if timeSeries[i] - timeSeries[i - 1] >= duration:
                res += duration
            else:
                res += timeSeries[i] - timeSeries[i - 1]
        res += duration
        return res


timeSeries = [1, 4]
duration = 2
result = Solution().findPoisonedDuration(timeSeries, duration)
print(result)
