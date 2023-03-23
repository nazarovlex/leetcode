class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_letters = {}
        for letter in ransomNote:
            if letter not in note_letters.keys():
                note_letters[letter] = 1
            elif letter in note_letters.keys():
                note_letters[letter] += 1
        for k, v in note_letters.items():
            if magazine.count(k) < v:
                return False
        return True


testcase_1 = ["a", "aa", "aa"]
testcase_2 = ["b", "ab", "aab"]

for i in range(len(testcase_1)):
    result = Solution().canConstruct(testcase_1[i], testcase_2[i])
    print(result)
