class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        level = 0
        go_down = True
        res = [""] * numRows

        for letter in s:
            res[level] += letter

            if level < numRows - 1 and go_down:
                level += 1
            elif level == 0 and not go_down:
                go_down = True
                level += 1
            elif level == numRows - 1 and go_down:
                go_down = False
                level -= 1
            elif level < numRows - 1 and not go_down:
                level -= 1

        return "".join(res)


s = "PAYPALISHIRING"
numRows = 1
result = Solution().convert(s, numRows)
print(result)
