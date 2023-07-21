from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet_morze = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
                          'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
                          'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
                          'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
        res = []
        for word in words:
            tmp = ""
            for letter in word:
                tmp += alphabet_morze[letter]
            res.append(tmp)
        return len(set(res))


words = ["gin", "zen", "gig", "msg"]
result = Solution().uniqueMorseRepresentations(words)
print(result)
