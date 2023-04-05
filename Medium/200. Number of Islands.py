from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def check_islands(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != '1':
                return

            grid[i][j] = "#"
            check_islands(grid,i+1,j)
            check_islands(grid,i-1,j)
            check_islands(grid,i,j+1)
            check_islands(grid,i,j-1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    check_islands(grid, i, j)
                    count += 1

        return count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
result = Solution().numIslands(grid)
print(result)
