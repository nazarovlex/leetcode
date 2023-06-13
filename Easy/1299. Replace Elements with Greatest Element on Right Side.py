from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        last_max = max(arr)
        for i in range(len(arr)):
            if i != len(arr) - 1:
                if last_max == arr[i]:
                    last_max = max(arr[i + 1:])
                    res.append(last_max)
                else:
                    res.append(last_max)
            else:
                res.append(-1)

        return res


arr = [17, 18, 5, 4, 6, 1]
result = Solution().replaceElements(arr)
print(result)
