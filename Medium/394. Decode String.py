class Solution:
    def decodeString(self, s: str) -> str:
        tmp = ""
        nums = []
        for i in range(len(s)):
            if s[i].isdigit():
                tmp += s[i]
            else:
                if len(tmp) > 0:
                    nums.append(int(tmp))
                    tmp = ""
        for num in nums[::-1]:
            digit_ind = s.rindex(str(num))
            open = s.index("[", digit_ind)
            close = s.index("]", digit_ind)
            s = s[:digit_ind] + num * s[open + 1:close] + s[close + 1:]

        return s


s = "3[a2[c]]"
result = Solution().decodeString(s)
print(result)
