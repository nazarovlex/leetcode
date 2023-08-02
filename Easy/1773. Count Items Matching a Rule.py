from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            ind = 0
        elif ruleKey == "color":
            ind = 1
        elif ruleKey == "name":
            ind = 2
        cnt = 0
        for item in items:

            if item[ind] == ruleValue:
                cnt += 1
        return cnt


items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
ruleKey = "type"
ruleValue = "phone"
result = Solution().countMatches(items, ruleKey, ruleValue)
print(result)
