# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def helper(node):
            if not node:
                return [math.inf,-1]
            
            minL,maxL = helper(node.left)
            minR, maxR = helper(node.right)

            minL,maxL = min(node.val,minL),max(node.val, maxL)
            minR,maxR = min(node.val,minR),max(node.val, maxR)

            self.ans = max(self.ans, abs(node.val - minL) ,abs(node.val -  maxL))
            self.ans = max(self.ans, abs(node.val - minR) ,abs(node.val -  maxR))

            return [min(minL, minR),max(maxL, maxR)]

        helper(root)
        return self.ans

        
        

        