from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # Long but fast
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(t1, t2):
            if t1 and t2:
                if t1.val != t2.val:
                    return False
            if t1 == None and t2 == None:
                return True
            elif t1 == None or t2 == None:
                return False
            if t1.left or t2.left:
                if t1.left and t2.left:
                    if not helper(t1.left, t2.left):
                        return False
                else:
                    return False
            if t1.right or t2.right:
                if t1.right and t2.right:
                    if not helper(t1.right, t2.right):
                        return False
                else:
                    return False
            return True

        return helper(p, q)


class Solution2:  # Easy but slower
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q


tree1 = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3), right=TreeNode(val=2)))
tree2 = TreeNode(val=1, left=TreeNode(val=0, left=TreeNode(val=1), right=TreeNode(val=2)))
result = Solution2().isSameTree(tree1, tree2)
print(result)
