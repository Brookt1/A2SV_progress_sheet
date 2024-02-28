# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic=Counter()
        def dfs(node):
            if node is None:
                return
            if node:
                dic[node.val]+=1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        
        max_val=max(dic.values())
        ans=[]
        for key,val in dic.items():
            if val == max_val:
                ans.append(key)

        return ans