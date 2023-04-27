class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) == k:
            return s[::-1]
        i = 0
        while i < len(s) - 1:
            s = s[:i] + s[i:i + k][::-1] + s[i + k:]
            i += k * 2
        return s


string = "abcdefg"  # bacdfeg
k = 2
result = Solution().reverseStr(string, k)
print(result)
