class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1)+int(num2))



testcase_1 = ["11", "456", "0"]
testcase_2 = ["123", "77", "0"]


for i in range(len(testcase_1)):
    result = Solution().addStrings(testcase_1[i],testcase_2[i])
    print(result)
