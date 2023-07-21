from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam = {}
        for log in logs:
            if log[0] not in uam:
                uam[log[0]] = [log[1]]
            else:
                if log[1] not in uam[log[0]]:
                    uam[log[0]] += [log[1]]

        res = [0] * k
        for v in uam.values():
            res[len(v) - 1] += 1
        return res


logs = [[1, 1], [2, 2], [2, 3]]
k = 5
result = Solution().findingUsersActiveMinutes(logs, k)
print(result)
