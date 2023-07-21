class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if ord(s[left]) > ord(s[right]):
                    s = s[:left] + s[right] + s[left + 1:]
                else:
                    s = s[:right] + s[left] + s[right + 1:]
            left += 1
            right -= 1
        return s


s = "egcfe"
result = Solution().makeSmallestPalindrome(s)
print(result)
