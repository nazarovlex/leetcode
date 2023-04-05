from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if target <= matrix[mid][-1] and target >= matrix[mid][0]:
                if target in matrix[mid]:
                    return True
                else:
                    return False
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                right = mid - 1


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
result = Solution().searchMatrix(matrix, target)
print(result)
