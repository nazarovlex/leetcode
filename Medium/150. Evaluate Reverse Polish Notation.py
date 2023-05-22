from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for ind, obj in enumerate(tokens):
                if obj == "+" or obj == "-" or obj == "*" or obj == "/":
                    if obj == "+":
                        res = int(tokens[ind - 2]) + int(tokens[ind - 1])
                        tokens = tokens[:ind - 2] + [str(res)] + tokens[ind + 1:]
                        break

                    elif obj == "-":
                        res = int(tokens[ind - 2]) - int(tokens[ind - 1])
                        tokens = tokens[:ind - 2] + [str(res)] + tokens[ind + 1:]
                        break

                    elif obj == "*":
                        res = int(tokens[ind - 2]) * int(tokens[ind - 1])
                        tokens = tokens[:ind - 2] + [str(res)] + tokens[ind + 1:]
                        break

                    elif obj == "/":
                        res = int(int(tokens[ind - 2]) / int(tokens[ind - 1]))
                        tokens = tokens[:ind - 2] + [str(res)] + tokens[ind + 1:]
                        break

        return int(tokens.pop())


tokens = ["2", "1", "+", "3", "*"]
result = Solution().evalRPN(tokens)
print(result)
