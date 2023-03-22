from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            if operations[i] == "+":
                res.append(sum(res[-2:]))
            elif operations[i] == "D":
                res.append(res[-1] * 2)
            elif operations[i] == "C":
                res.pop(-1)
            else:
                res.append(int(operations[i]))
        return sum(res)


class Solution2:  # 1st solution method, without adding array
    def calPoints(self, operations: List[str]) -> int:
        for i in range(len(operations)):
            if operations[i] == "+":
                operations[i] = operations[i - 1] + operations[i - 2]

            elif operations[i] == "D":
                operations[i] = operations[i - 1] * 2

            elif operations[i] == "C":
                operations.pop(i)
                operations.insert(0, 0)

                operations.pop(i)
                operations.insert(0, 0)
            else:
                operations[i] = int(operations[i])
        return sum(operations)


ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
result = Solution2().calPoints(ops)
print(result)
