class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        res = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                res += 1

        return res


startTime = [1, 2, 3]
endTime = [3, 2, 7]
queryTime = 4
result = Solution().busyStudent(startTime, endTime, queryTime)
print(result)
