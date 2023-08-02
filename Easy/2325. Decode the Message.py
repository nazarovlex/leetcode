class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")
        alphabit = {}
        i = 97
        for letter in key:
            if letter.isalpha() and letter not in alphabit:
                alphabit[letter] = chr(i)
                i += 1
        res = ""
        for letter in message:
            if letter.isalpha():
                res += alphabit[letter]
            else:
                res += letter
        return res


key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
result = Solution().decodeMessage(key, message)
print(result)
