# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes=[]

        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            if node:
                nodes.append(node.val)
            inorder(node.right)
        inorder(root)
        return len(nodes) == len(set(nodes)) and nodes == sorted(nodes)
        