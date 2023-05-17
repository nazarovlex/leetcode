from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for num in arr:
            if arr.count(num)/len(arr)>0.25:
                return num


arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
result = Solution().findSpecialInteger(arr)
print(result)
