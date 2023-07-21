from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        if len(arr) % 2 == 1:
            res += sum(arr)

        for i in range(1, len(arr), 2):
            for j in range(len(arr) - i + 1):
                res += sum(arr[j:j + i])
        return res


arr = [1, 4, 2, 5, 3]
result = Solution().sumOddLengthSubarrays(arr)
print(result)
