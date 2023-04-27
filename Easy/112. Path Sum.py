from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        cnt = 0
        mas = []

        def helper(tree, cnt, mas):
            if tree:
                cnt += tree.val

                if tree.left:
                    helper(tree.left, cnt, mas)
                if tree.right:
                    helper(tree.right, cnt, mas)
                if not tree.left and not tree.right:
                    mas.append(cnt)

        helper(root, cnt, mas)
        return True if targetSum in mas else False


t = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=1)), right=TreeNode(val=4))
target = 5
result = Solution().hasPathSum(t, target)
print(result)
