# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:



        def search(node):
            if node is None:
                return None

            if node.val == val:
                return node
            elif node.val<val:
                node = search(node.right)
            else:
                node = search(node.left)
            return node
        return search(root)
        