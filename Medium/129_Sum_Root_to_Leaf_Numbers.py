# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumNumbers(self, root):
        def left(root, c):
            while root:
                c = c*10 + root.val
                root = root.left
            cnt.append(c)
            c = 0
        def right(root, c):
            while root:
                c = c*10 + root.val
                root = root.right
            cnt.append(c)
            c = 0
        def add_number(root,c):
            while root:
                print(cnt)
                left(root,c)

                add_number(root.left,c)

                # else:
                #     add_number(root.left,c)
                #     add_number(root.right,c)
        cnt = []
        c = 0
        add_number(root,c)

        print(cnt)
        return sum(cnt)


# tree = TreeNode(val=4, left=TreeNode(val=9, left=TreeNode(val=5), right=TreeNode(val=1)), right=TreeNode(val=0))
tree = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
result = Solution().sumNumbers(tree)
print(result)
