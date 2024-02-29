# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.n = 1
        self.ans = -1

        
        def inorder(node):
            if node is None:
                return
            
            
            inorder(node.left)
            if self.n == k:
                self.ans = node.val
            self.n += 1
            inorder(node.right)

        inorder(root)
        

        return self.ans
        