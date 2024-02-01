# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        evenNode=even=ListNode()
        oddNode=odd=ListNode()
        while head and head.next:
            evenNode.next=head.next
            oddNode.next=head
            evenNode=evenNode.next
            oddNode=oddNode.next
            head=head.next.next
        print()
        if head:
            oddNode.next=head
            oddNode=oddNode.next
        oddNode.next=even.next
        evenNode.next=None
        return odd.next
                
        