class Solution:
    def maximum69Number(self, num: int) -> int:
        num = str(num)
        if num.count("6") != 0:
            first_six = num.index("6")
            num = num[:first_six] + "9" + num[first_six + 1:]

        return int(num)


n = 96699
result = Solution().maximum69Number(n)
print(result)
