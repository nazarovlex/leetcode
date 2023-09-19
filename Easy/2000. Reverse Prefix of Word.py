class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for ind, letter in enumerate(word):
            if ind == len(word) - 1 and letter != ch:
                ind = 0
                break
            if letter == ch:
                break

        word = word[:ind + 1][::-1] + word[ind + 1:]
        return word


word = "abcdefd"
ch = "d"
result = Solution().reversePrefix(word, ch)
print(result)
