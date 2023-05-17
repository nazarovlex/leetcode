from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # line
        for line in board:
            for number in line:
                if number.isdigit():
                    if line.count(number) > 1:
                        return False
        # column
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            for num in column:
                if num.isdigit():
                    if column.count(num) > 1:
                        return False
        # box 3x3
        for i in range(0, 9, 3):
            for kj in range(0, 9, 3):
                box = []
                for ki in range(3):
                    for j in range(3):
                        box.append(board[i + ki][j + kj])

                for num in box:
                    if num.isdigit():
                        if box.count(num) > 1:
                            return False

        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
result = Solution().isValidSudoku(board)
print(result)
