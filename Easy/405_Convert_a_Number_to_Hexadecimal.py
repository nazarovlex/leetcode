class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            return hex(2 ** 32 + num)[2:]
        return hex(abs(num))[2:]


testcase = [26, -1]
answers = ["1a", "ffffffff"]
for i in range(len(testcase)):
    result = Solution().toHex(testcase[i])
    if result != answers[i]:
        print(f"False the {testcase[i]} in hex is {answers[i]}. Your answer is {result}")
