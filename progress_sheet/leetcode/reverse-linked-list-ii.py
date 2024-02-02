# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy=ListNode()
        dummy.next=head
        cur=head
        prev=dummy
        for _ in range(left-1):
            prev=cur
            cur=cur.next
        last=prev
        prev=cur
        cur=cur.next
        count=left
        while count<right:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            count+=1
        last.next.next=cur
        last.next=prev
        return dummy.next
            
