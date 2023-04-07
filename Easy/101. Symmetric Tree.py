from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(t1, t2):
            if t1 and t2:
                return t1.val == t2.val and helper(t1.left, t2.right) and helper(t1.right, t2.left)
            return t1 is t2

        return helper(root.left, root.right)


tree = TreeNode(val=1,
                left=TreeNode(val=2, left=TreeNode(val=2)),
                right=TreeNode(val=2, right=TreeNode(val=3)))

result = Solution().isSymmetric(tree)
print(result)
