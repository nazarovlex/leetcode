class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        for i in range(len(s)):
            if s[i].isdigit():
                res += s[i]
            elif s[i].isalpha() or s[i] == ".":
                break
            elif s[i] == " " and len(res) == 0:
                continue
            elif s[i] == "-" and "+" in res or s[i] == "+" and "-" in res:
                break
            elif s[i] == "+" and len(res) == 0:
                res += s[i]
            elif s[i] == "-" and len(res) == 0:
                res += s[i]
            else:
                break
        if len(res) == 1 and res[0] == "-" or len(res) == 1 and res[0] == "+":
            return 0
        if len(res) > 0:
            if int(res) > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif int(res) < -2 ** 31:
                return -2 ** 31
            else:
                return int(res)

        else:
            return 0


s = "2147483648"
result = Solution().myAtoi(s)
print(result)
