from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def find_depth(t, cnt):
            if t is None:
                return 0
            else:
                left = find_depth(t.left, cnt + 1)
                right = find_depth(t.right, cnt + 1)
                if left < 0 or right < 0 or abs(left - right) > 1:
                    return -1
                return max(left, right) + 1
        return find_depth(root, 0) >= 0


tree = TreeNode(val=5,left=TreeNode(val=4, left=TreeNode(val=11, left=TreeNode(val=7), right=TreeNode(val=2))),right=TreeNode(val=8, left=TreeNode(val=13),right=TreeNode(val=4, left=TreeNode(val=5), right=TreeNode(val=1))))

result = Solution().isBalanced(tree)
print(result)
