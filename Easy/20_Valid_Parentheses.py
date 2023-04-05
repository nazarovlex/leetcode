class Solution(object):
    def isValid(self, s):
        opened_brackets = ["(", "[", "{"]
        closed_brackets = [")", "]", "}"]
        if len(s)%2>0 or s[0] in closed_brackets or s[-1] in opened_brackets:
            return False
        i = 1
        while i<len(s):
            if s[i] in closed_brackets and s[i-1] != opened_brackets[closed_brackets.index(s[i])]:
                return False

            elif s[i] in closed_brackets and s[i-1] == opened_brackets[closed_brackets.index(s[i])]:
                s = s[:i-1] + s[i+1:]
                i = 0
                continue
            elif i == len(s)-1 and len(s)>0:
                return False
            i += 1
        return True


class Solution2:
    def isValid(self, s: str) -> bool:
        if len(s) % 2: return False
        stack = []
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or pairs[stack.pop()] != bracket:
                return False
        return len(stack) == 0


s = "()[]{}"
result = Solution().isValid(s)
print(result)
