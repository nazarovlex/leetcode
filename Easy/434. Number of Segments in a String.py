class Solution:
    def countSegments(self, s: str) -> int:
        return s.count(" ") + 1 if len(s) > 0 else 0


s = "Hello, my name is John"
result = Solution().countSegments(s)
print(result)
