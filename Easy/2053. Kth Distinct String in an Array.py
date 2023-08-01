from typing import List
from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        data = {}
        data = dict(Counter(arr))
        result = list(filter(lambda x: data[x] == 1, data))
        if len(result) < k:
            return ''
        return result[k - 1]

arr = ["d", "b", "c", "b", "c", "a"]
k = 2
result = Solution().kthDistinct(arr, k)
print(result)