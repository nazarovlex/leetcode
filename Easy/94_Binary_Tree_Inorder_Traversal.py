# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    l1 = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        self.inorderTraversal(root.left)
        self.l1.append(root.val)
        self.inorderTraversal(root.right)
        res = self.l1
        l1 = []
        return res


tree = TreeNode(val=1, left=TreeNode(val=3, right=TreeNode(val=2)))

s = Solution()
result = s.inorderTraversal(root=tree)
print(result)
