class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False


number = 101
result = Solution().isPalindrome(number)
print(result)