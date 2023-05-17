class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('a' 'e' 'i' 'o' 'u''A' 'E' 'I' 'O' 'U')
        stack = []
        for letter in s:
            if letter in vowels:
                stack.append(letter)
        for i in range(len(s)):
            if s[i] in vowels:
                s = s[:i]+stack.pop()+s[i+1:]

        return s


s = "hello"
result = Solution().reverseVowels(s)
print(result)