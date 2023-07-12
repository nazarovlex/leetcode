from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies[:i] + candies[i + 1:]):
                res.append(True)
            else:
                res.append(False)
        return res


candies = [12, 1, 12]
extraCandies = 10
result = Solution().kidsWithCandies(candies, extraCandies)
print(result)
