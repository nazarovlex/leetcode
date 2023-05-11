from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_ind = []
        for ind_1, nums in enumerate(matrix):
            for ind_2, num in enumerate(nums):
                if num == 0:
                    zero_ind.append([ind_1, ind_2])
        print(zero_ind)
        for ind in zero_ind:
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if i == ind[0] or j == ind[1]:
                        matrix[i][j] = 0
        print(matrix)


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
