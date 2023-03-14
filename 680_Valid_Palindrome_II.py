class Solution(object):
    def validPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                s1 = s[start:end]
                s2 = s[start + 1:end + 1]
                if s2 == s2[::-1]:
                    return True
                elif s1 == s1[::-1]:
                    return True
                else:
                    return False

            start += 1
            end -= 1
        return True


string = "errcef"
result = Solution().validPalindrome(string)
print(result)
