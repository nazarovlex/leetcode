class Solution:
    def makeFancyString(self, s: str) -> str:
        cnt = 1
        prev = s[0]
        res_s = prev
        for i in range(1, len(s)):
            if s[i] == prev:
                cnt += 1
                if cnt < 3:
                    res_s += s[i]
            else:
                prev = s[i]
                cnt = 1
                res_s += s[i]
        return res_s


s = "leeetcode"
result = Solution().makeFancyString(s)
print(result)
