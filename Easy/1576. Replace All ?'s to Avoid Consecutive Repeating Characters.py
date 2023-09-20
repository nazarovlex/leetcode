class Solution:
    def modifyString(self, s: str) -> str:
        if s == '?':
            return "a"
        for ind, letter in enumerate(s):
            if letter == "?":
                if len(s)-1 > ind > 0:
                    new_chr = 97
                    while new_chr == ord(s[ind-1]) or new_chr == ord(s[ind+1]):
                        new_chr += 1
                    s = s[:ind] + chr(new_chr) + s[ind+1:]
                elif ind == 0:
                    new_chr = 97
                    while new_chr == ord(s[ind + 1]):
                        new_chr += 1
                    s = chr(new_chr) + s[ind + 1:]
                else:
                    new_chr = 97
                    while new_chr == ord(s[ind - 1]) :
                        new_chr += 1
                    s = s[:ind] + chr(new_chr)
        return s



s = "?"
result = Solution().modifyString(s)
print(result)