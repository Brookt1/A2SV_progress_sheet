# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        visted=set()

        while headA or headB:
            if headA:
                if headA in visted: return headA
                visted.add(headA)
                headA=headA.next
            if headB:
                if headB in visted: return headB
                visted.add(headB)
                headB=headB.next
        
            
        