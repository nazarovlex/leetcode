from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for i in range(k):
            for i in range(len(grid)):
                grid[i].insert(0, grid[i - 1].pop())
        return grid


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
result = Solution().shiftGrid(grid, k)
print(result)
