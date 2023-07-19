from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        for interval in intervals:
            if newInterval[0] <= interval[1] and newInterval[1] >= interval[0]:
                interval[0] = min(interval[0], newInterval[0])
                interval[1] = max(interval[1], newInterval[1])
                break
            elif newInterval[0] < interval[1] and newInterval[1] < interval[1]:
                intervals.insert(intervals.index(interval), newInterval)
                break
            elif newInterval[0] > intervals[-1][1]:
                intervals.append(newInterval)
                break
            elif newInterval[1] < intervals[0][0]:
                intervals.insert(0, newInterval)
                break
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                tmp = [res[-1][0], max(res[-1][1], intervals[i][1])]
                res.pop()
                res.append(tmp)
            else:
                res.append(intervals[i])

        return res


intervals = [[3, 5], [12, 15]]
newInterval = [6, 6]
result = Solution().insert(intervals, newInterval)
print(result)
