class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])




string = "Hello World"
result = Solution().lengthOfLastWord(string)
print(result)