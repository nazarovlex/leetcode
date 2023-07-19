from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop(-1)
                i += 1
            i += 1


arr = [1, 0, 2, 3, 0, 4, 5, 0]
result = Solution().duplicateZeros(arr)
print(arr)
