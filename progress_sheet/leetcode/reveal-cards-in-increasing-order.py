class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:


        deck.sort()
        ans=deque()
        for i in range(len(deck)-1,0,-1):
            ans.append(deck[i])
            val=ans.popleft()
            ans.append(val)
        ans.append(deck[0])
        ans.reverse()

        return ans

        
        