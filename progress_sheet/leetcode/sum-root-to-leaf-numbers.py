# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.path = []

        def helper(node):

            if node.left is None and node.right is None:
                self.ans += int(''.join(str(val) for val in self.path) + str(node.val))
                return

            
            self.path.append(node.val)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            self.path.pop()
        helper(root)
        return self.ans

