from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution: # Recursion solution
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None: return root2
        if root2 is None: return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


tree1 = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3), right=TreeNode(val=2)))
tree2 = TreeNode(val=1, left=TreeNode(val=0, left=TreeNode(val=1), right=TreeNode(val=2)))
result = Solution().mergeTrees(tree1, tree2)
def print_tree(tree):
    print(tree.val)
    if tree.left:
        print_tree(tree.left)
    if tree.right:
        print_tree(tree.right)
print_tree(result)