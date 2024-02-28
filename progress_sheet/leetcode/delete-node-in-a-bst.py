# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:



        def delete(node,val):
            if node is None:
                return None

            if node.val > val:
                node.left = delete(node.left,val)

            elif node.val < val:
                node.right = delete(node.right,val)
            
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                print(node.val)
                temp = min_val(node.right)
                delete(node,temp.val)
                node.val = temp.val
            
            return node
        def min_val(node):
            while node.left:
                node=node.left
            return node

        return delete(root,key)