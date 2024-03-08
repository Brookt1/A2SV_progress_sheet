# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        dic = {}
        def helper(n, depth, node):
            if node is None:
                return
            
            if depth in dic:
                _min, _max = dic[depth]
                dic[depth] = [min(_min, n), max(_max, n)]
            else:
                dic[depth] = [n, n]
            helper(n*2, depth + 1, node.left)
            helper(n*2 + 1, depth + 1, node.right)
        
        helper(1, 0, root)
        ans = 0
        for _min, _max in dic.values():
            ans = max(_max - _min + 1, ans)
        return ans



