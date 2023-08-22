class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = s.count(letter)
        return int(cnt / len(s) * 100)


s = "foobar"
letter = "o"
result = Solution().percentageLetter(s, letter)
print(result)
