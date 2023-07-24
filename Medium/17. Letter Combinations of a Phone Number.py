from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dict = {
            "1": [""],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            "0": [" "],
        }
        res = []
        def helper(digits_string: str, res_string: str):
            if digits_string == "":
                res.append(res_string)
                return
            for letter in dict[digits_string[0]]:
                helper(digits_string[1:], res_string+letter)


        helper(digits,"")
        return res




digits = "2"
result = Solution().letterCombinations(digits)
print(result)
