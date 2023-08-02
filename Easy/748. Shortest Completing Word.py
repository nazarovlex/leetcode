from typing import List
from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_plate = ""
        for letter in licensePlate.lower():
            if letter.isalpha():
                license_plate += letter

        res_word = ""
        change_cnt = 2 * 32

        license_plate_counter = Counter(license_plate)
        for word in words:
            cnt = 0
            for k, v in license_plate_counter.items():
                if word.count(k) < v:
                    cnt = -1
                    break
                elif word.count(k) >= v:
                    cnt += word.count(k) - v

            if cnt == -1:
                pass
            else:
                cnt += len(word) - len(license_plate) - cnt
                if cnt < change_cnt:
                    change_cnt = cnt
                    res_word = word
        return res_word


licensePlate = "e490936"
words = ["involve", "those", "else", "violence", "six", "positive", "product", "expect", "close", "couple"]
result = Solution().shortestCompletingWord(licensePlate, words)
print(result)
