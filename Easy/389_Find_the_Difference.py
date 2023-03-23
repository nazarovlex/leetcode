class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = {}
        for letter in s:
            if letter not in letters.keys():
                letters[letter] = 1
            else:
                letters[letter] += 1
        for letter in t:
            if letter not in letters.keys():
                return letter
            elif letters[letter] != t.count(letter):
                return letter
        return ""


testcase_1 = ["abcd", ""]
testcase_2 = ["abcde", "y"]

for i in range(len(testcase_1)):
    result = Solution().findTheDifference(testcase_1[i], testcase_2[i])
    print(result)
