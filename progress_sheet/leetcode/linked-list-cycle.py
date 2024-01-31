# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast,slow=head,head
        visted=set()
        while fast and fast.next:
            if fast in visted:
                return True
            visted.add(slow)
            fast=fast.next.next
            slow=slow.next
        return False
