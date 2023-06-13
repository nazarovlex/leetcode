from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []
        tup = list((x, names[ind]) for ind, x in enumerate(heights))
        tup.sort(reverse=True)
        for obj in tup:
            res.append(obj[1])
        return res


names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
result = Solution().sortPeople(names, heights)
print(result)
