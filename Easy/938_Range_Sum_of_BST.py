from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root, res):
            if root:
                helper(root.left, res)
                if low <= root.val <= high:
                    res.append(root.val)
                helper(root.right, res)

        res = []
        helper(root, res)
        return sum(res)


tree = TreeNode(val=10, left=TreeNode(val=5, left=TreeNode(val=3), right=TreeNode(val=7)),
                right=TreeNode(val=15, right=TreeNode(val=18)))
low, high = 7, 15
result = Solution().rangeSumBST(tree, low, high)
print(result)
