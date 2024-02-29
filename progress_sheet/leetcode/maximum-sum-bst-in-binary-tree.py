# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class data:
    def __init__(self, max_left = -math.inf, min_right = math.inf, sum = 0,isBST = True):

        self.max_left = max_left
        self.min_right = min_right
        self.sum = sum
        self.isBST = isBST

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:


        self.ans = 0 

        def helper(node):

            if node is None:
                return data()
            

            left_data = helper(node.left)
            right_data = helper(node.right)

            val = data()
            val.isBST = left_data.isBST and right_data.isBST and left_data.max_left < node.val and node.val < right_data.min_right
            val.sum = left_data.sum + right_data.sum + node.val

            if val.isBST:
                self.ans = max(self.ans, val.sum)

            val.max_left = max(left_data.max_left, right_data.max_left, node.val)
            val.min_right =min(right_data.min_right, left_data.min_right, node.val)


            return val

        helper(root)

        return self.ans

            

            
        