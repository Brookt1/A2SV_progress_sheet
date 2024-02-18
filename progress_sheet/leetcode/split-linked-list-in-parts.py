# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        node=head
        n=0
        while node: 
            n+=1
            node=node.next
        
        rem=n%k
        res=[]
        node=head
        while node:
            temp=node
            for i in range(n//k-1):
                temp=temp.next
            if n//k >0 and rem>0:
                temp=temp.next
                rem-=1
            res.append(node)
            if temp:
                node=temp.next
                temp.next=None
            else:
                break
        for i in range(k-len(res)):
            res.append(None)
        return res
        

            
        