from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(t, sum, res):
            if not t:
                return
            sum = sum * 10 + t.val
            if not t.right and not t.left:
                res.append(sum)
            helper(t.left, sum, res)
            helper(t.right, sum, res)
            sum -= t.val

        res = []
        helper(root, 0, res)
        return sum(res)


tree = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3), right=TreeNode(val=2)))
result = Solution().sumNumbers(tree)
print(result)
