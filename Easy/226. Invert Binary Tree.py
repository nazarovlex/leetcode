from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(right, left):
            right, left = left, right
            if right:
                if right.right and right.left:
                    right.right, right.left = helper(right.right, right.left)
            if left:
                if left.right and left.left:
                    left.right, left.left = helper(left.right, left.left)
            return right, left

        if not root or not root.right and not root.left:
            return root

        root.right, root.left = helper(root.right, root.left)
        return root


def print_tree(t):
    print(t.val, end=" ")
    if t.left:
        print_tree(t.left)
    if t.right:
        print_tree(t.right)


tree = TreeNode(val=2, left=TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=4)),
                right=TreeNode(val=3, left=TreeNode(val=2), right=TreeNode(val=5)))

print_tree(tree)
result = Solution().invertTree(tree)
print()
print_tree(result)
