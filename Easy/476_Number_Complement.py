class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)
        num = num[2:]
        num2 = ""
        for i in range(len(num)):
            if num[i] == "0":
                num2 += "1"
            elif num[i] == "1":
                num2 += "0"

        return int(num2, 2)


n = 6
result = Solution().findComplement(n)
print(result)
