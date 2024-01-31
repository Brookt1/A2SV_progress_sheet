# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        less_dummy=ListNode()
        great_dummy=ListNode()
        less_tail=less_dummy
        great_tail=great_dummy
        node=head
        while node:
            if node.val>=x:
                great_tail.next=node
                great_tail=great_tail.next
            else:
                less_tail.next=node
                less_tail=less_tail.next
            node=node.next
        great_tail.next=None
        less_tail.next=great_dummy.next
        return less_dummy.next



        