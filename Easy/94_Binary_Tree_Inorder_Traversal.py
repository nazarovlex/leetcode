# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        def helper(root, res):
            if root:
                helper(root.left, res)
                res.append(root.val)
                helper(root.right, res)

        res = []
        helper(root, res)
        return sum(res)


tree = TreeNode(val=1, left=TreeNode(val=3, right=TreeNode(val=2)))

result = Solution().inorderTraversal(root=tree)
print(result)
