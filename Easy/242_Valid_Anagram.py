class Solution(object):
    def isAnagram(self, s, t):
        s_dict = {}
        t_dict = {}
        for letter in set(s):
            if letter not in s_dict:
                s_dict[letter] = s.count(letter)

        for letter in set(t):
            if letter not in t_dict:
                t_dict[letter] = t.count(letter)
        if s_dict == t_dict:
            return True
        else:
            return False


s = "anagram"
t = "nagaram"
result = Solution().isAnagram(s, t)
print(result)
