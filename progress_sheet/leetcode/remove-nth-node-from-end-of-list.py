# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        count=1
        dummy=ListNode()
        dummy.next=head
        left,right=dummy,head
        while right:
            if count>n:
                left=left.next
            count+=1
            right=right.next
        left.next=left.next.next
        return dummy.next
        
