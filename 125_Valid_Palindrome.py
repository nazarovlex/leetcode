class Solution(object):
    def isPalindrome(self, s):
        new_s = ""
        for letter in s:
            if letter.isalpha():
                new_s += letter
            elif letter.isdigit():
                new_s += letter
        s = new_s.lower()
        if s == s[::-1]:
            return True
        else:
            return False


string = "1A man, a plan, a canal: Panama1"
result = Solution().isPalindrome(string)
print(result)
