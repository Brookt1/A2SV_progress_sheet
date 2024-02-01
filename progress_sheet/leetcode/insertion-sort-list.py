# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur=head.next
        tail=head
        while cur:
            if cur.val>tail.val:
                tail.next=cur
                tail=tail.next
                cur=cur.next
                continue
            
            temp=head
            prev=head
            while cur and temp and cur.val>temp.val:
                prev=temp
                temp=temp.next
            next=cur.next
            if temp==head:
                head=cur
                cur.next=prev
            else:
                prev.next=cur
                cur.next=temp
            cur=next
        tail.next=None
        return head




            



        