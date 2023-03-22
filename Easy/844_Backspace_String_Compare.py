class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s2, t2 = "", ""
        for i in range(len(s)):
            if s[i] != "#":
                s2 += s[i]
            elif s[i] == "#" and i > 0:
                s2 = s2[:-1]
        for i in range(len(t)):
            if t[i] != "#":
                t2 += t[i]
            elif t[i] == "#" and i > 0:
                t2 = t2[:-1]
        if s2 == t2:
            return True
        return False


class Solution2:  # Faster and less memory used
    def backspaceCompare(self, s: str, t: str) -> bool:
        while s.count("#") > 0:
            if s.index("#") == 0:
                s = s[1:]
            else:
                s = s[:s.index("#") - 1] + s[s.index("#") + 1:]
        while t.count("#") > 0:
            if t.index("#") == 0:
                t = t[1:]
            else:
                t = t[:t.index("#") - 1] + t[t.index("#") + 1:]
        if s == t:
            return True
        return False


s, t = "a##c", "#a#c"
result = Solution().backspaceCompare(s, t)
print(result)
result = Solution2().backspaceCompare(s, t)
print(result)
