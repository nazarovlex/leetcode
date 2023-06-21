class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for number in num[::-1]:
            if number == "0":
                num = num[:-1]
            else:
                break
        return num


num = "51230100"
result = Solution().removeTrailingZeros(num)
print(result)
