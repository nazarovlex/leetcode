from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        res = []
        i = 0
        intervals.sort()

        while i < len(intervals):
            if len(res) == 0 or intervals[i][0] > res[-1][-1]:
                res.append(intervals[i])
            elif intervals[i][0] <= res[-1][-1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            i += 1

        return res


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = Solution().merge(intervals)
print(result)
