class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            if s[i] != "#":
                res += chr(int(s[i]) + 96)
            else:
                res = res[:-2]
                res += chr(int(s[i-2:i]) + 96)

        return res


s = "1326#"
result = Solution().freqAlphabets(s)
print(result)
