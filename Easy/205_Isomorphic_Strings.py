class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letters = {}
        for i in range(len(s)):
            if s[i] not in letters.keys() and t[i] not in letters.values():
                letters[s[i]] = t[i]
            elif s[i] in letters.keys() and t[i] not in letters.values():
                return False
            elif s[i] not in letters.keys() and t[i] in letters.values():
                return False
            elif letters[s[i]] != t[i]:
                return False
        return True


testcase = {"egg": "add", "foo": "bar", "paper": "title", "bbbaaaba": "aaabbbba"}
for k, v in testcase.items():
    result = Solution().isIsomorphic(k, v)
    print(result)
