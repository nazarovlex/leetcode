from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter = Counter(s)
        cnt = int(counter[target[0]] / target.count(target[0]))
        for letter in set(target[1:]):
            if counter[letter] < cnt:
                cnt = int(counter[letter] / target.count(letter))

        return cnt


s = "abbaccaddaeea"
target = "aaaaa"
result = Solution().rearrangeCharacters(s, target)
print(result)
