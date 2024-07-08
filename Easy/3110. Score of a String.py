class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        prev = s[0]
        for letter in s[1:]:
            res += abs(ord(prev) - ord(letter))
            prev = letter
        return res


s = "hello"
result = Solution().scoreOfString(s)
print(result)
