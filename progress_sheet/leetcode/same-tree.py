# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def helper(root1,root2):
            if root1 is None or root2 is None:
                return root1 is None and root2 is None
            
            left = helper(root1.left,root2.left)
            right = helper(root1.right,root2.right)

            if not left or not right  or root1.val != root2.val:
                return False

            return True
        return helper(p,q)
        