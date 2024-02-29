# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return None

        queue = deque()
        queue.append(root)
        res=[]

        while queue:
            level_res = []
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                level_res.append(node.val)
            if len(res) % 2 != 0:
                res.append(reversed(level_res))
            else:
                res.append(level_res)
        return res