class Solution:
    def reverseBits(self, n):
        s = bin(n)
        s = s[2:]
        s = s[::-1] + ("0" * (32 - len(s)))
        return int(s, 2)


number = int("00000010100101000001111010011100", 2)  # res = 964176192
result = Solution().reverseBits(number)
print(result)
