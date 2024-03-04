# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:




        def helper(left, right):

            if left > right:
                return None
            
            max_idx = left
            for i in range(left + 1,right + 1):
                if nums[i] > nums[max_idx]:
                    max_idx = i
            node = TreeNode(nums[max_idx])
            node.left = helper(left, max_idx-1)
            node.right = helper(max_idx + 1, right)

            return node
        return helper(0,len(nums)-1)
        