class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            if columnNumber % 26 > 0:
                res += chr(columnNumber % 26 + 64)
                columnNumber = (columnNumber - columnNumber % 26) // 26
            elif columnNumber % 26 == 0 and columnNumber > 26:
                res += "Z"
                columnNumber = (columnNumber - 1) // 26
            else:
                res += chr(columnNumber + 64)
                break
        return res[::-1]


testcase = {701: "ZY", 1: "A", 2: "B", 3: "C", 28: "AB", 2147483647: "FXSHRXW", 52: "AZ"}
for test in testcase:
    result = Solution().convertToTitle(test)
    if result != testcase[test]:
        print(f"EXPECTED:{testcase[test]} \nOUTPUT: {result} ")

# result = Solution().convertToTitle(701)
# print(result)
