class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictionary = {}
        if len(pattern) != len(s.split(" ")):
            return False
        for i in range(len(pattern)):
            tmp = s.split(" ")[i]
            if tmp not in dictionary.values() and pattern[i] not in dictionary.keys():
                dictionary[pattern[i]] = tmp
            elif tmp in dictionary.values() and pattern[i] not in dictionary.keys():
                return False
            elif tmp not in dictionary.values() and pattern[i] in dictionary.keys():
                return False
            elif tmp in dictionary.values() and pattern[i] in dictionary.keys():
                if dictionary[pattern[i]] != tmp:
                    return False
        return True


testcase_1 = ["abba", "abba", "aaaa"]
testcase_2 = ["dog cat cat dog", "dog cat cat fish", "dog cat cat dog"]

for i in range(len(testcase_1)):
    result = Solution().wordPattern(testcase_1[i], testcase_2[i])
    print(result)
