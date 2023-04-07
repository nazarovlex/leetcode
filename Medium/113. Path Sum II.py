from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self,root, target, res, tmp):
        if not root:
            return
        tmp.append(root.val)

        if not root.left and not root.right and root.val == target:
            res.append(tmp[:])

        self.helper(root.left, target-root.val, res, tmp)
        self.helper(root.right, target-root.val, res, tmp)
        tmp.pop(-1)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.helper(root, targetSum, res, [])
        return res






tree = TreeNode(val=5,
                left=TreeNode(val=4, left=TreeNode(val=11, left=TreeNode(val=7), right=TreeNode(val=2))),
                right=TreeNode(val=8, left=TreeNode(val=13),
                               right=TreeNode(val=4, left=TreeNode(val=5), right=TreeNode(val=1))))
target = 22
result = Solution().pathSum(tree, target)
print(result)
