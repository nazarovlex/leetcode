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


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    i, j = i + 1, j - 1
                    continue
            i, j = i + (not a.isalnum()), j - (not b.isalnum())
        return True


string = "1A man, a plan, a canal: Panama1"
result = Solution().isPalindrome(string)
print(result)
result = Solution2().isPalindrome(string)
print(result)
