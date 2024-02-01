# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return 
        prev=head
        node=head.next
        while node:
            if node.val==prev.val:
                prev.next=node.next
            else:
                prev=prev.next
            node=node.next

        return head