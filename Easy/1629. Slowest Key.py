from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_num, max_ind = releaseTimes[0], 0
        for ind in range(1, len(releaseTimes)):
            cur_num = releaseTimes[ind] - releaseTimes[ind - 1]
            if max_num < cur_num:
                max_num = cur_num
                max_ind = ind
            elif max_num == cur_num:
                if ord(keysPressed[ind]) > ord(keysPressed[max_ind]):
                    max_num = cur_num
                    max_ind = ind
        return keysPressed[max_ind]


releaseTimes = [23, 34, 43, 59, 62, 80, 83, 92, 97]
keysPressed = "qgkzzihfc"
result = Solution().slowestKey(releaseTimes, keysPressed)
print(result)
