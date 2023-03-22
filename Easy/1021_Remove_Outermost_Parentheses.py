class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened, closed = 0, 0
        i = 0
        res = ""
        while i < len(s):
            if s[i] == "(":
                opened += 1
            elif s[i] == ")":
                closed += 1
            if opened == closed:
                res += s[1:i]
                opened, closed = 0, 0
                s = s[i + 1:]
                i = 0
                continue
            i += 1
        return res


class Solution2:
    def removeOuterParentheses(self, s: str) -> str:
        i = 0
        res = ""
        while i < len(s):
            if s[:i + 1].count("(") == s[:i + 1].count(")"):
                res += s[1:i]
                s = s[i + 1:]
                i = 0
                continue
            i += 1
        return res


string = "(()())(())"
result = Solution().removeOuterParentheses(string)
print(result)
result = Solution2().removeOuterParentheses(string)
print(result)
