# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        


        dic={}
        def dfs(node , row , col):
            if node is None:
                return
            
            if col in dic:
                dic[col].append((row,node.val))
            else:
                dic[col] = [(row , node.val)]
            dfs(node.left , row +1, col -1 )
            dfs(node.right , row + 1 , col +1)

        dfs(root , 0 , 0)

        ans = []

        for key in sorted(dic.keys()):

            res =[]
            for row , val in sorted(dic[key]):
                res.append(val)
            ans.append(res)

        return ans
