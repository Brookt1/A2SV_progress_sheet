# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        nums = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        
        inorder(root)

        def bst(l, r):
            if r - l +1 == 1:
                return TreeNode(nums[r])
            if r - l + 1 < 1:
                return None
            mid = (r + l)//2
            node = TreeNode(nums[mid])
            node.left = bst(l, mid - 1)
            node.right = bst(mid + 1, r)
            return node
        return bst(0,len(nums)-1)