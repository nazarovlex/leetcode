class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            if s[i].lower() == s[i + 1].lower():
                if s[i].isupper() and s[i + 1].islower() or s[i].islower() and s[i + 1].isupper():
                    s = s[:i] + s[i + 2:]
                    if i > 0:
                        i -= 1
                    else:
                        i = 0
                    continue
            i += 1
        return s


testcase = ["leEeetcode", "abBAcC", "s", "mC"]
for string in testcase:
    result = Solution().makeGood(string)
    print(result)
