# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def trav(node):
            if node is None:
                return 0
            
            left = trav(node.left)
            right = trav(node.right)
            if node.val >= low and node.val <= high:
                left +=node.val
            return left + right
        return trav(root)
