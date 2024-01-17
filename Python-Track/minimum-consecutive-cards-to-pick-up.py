class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        visted=set()
        left=0
        res=len(cards)+1
        for right in range(len(cards)):
            if cards[right] in visted:
                while cards[right] in visted:
                    visted.remove(cards[left])
                    left+=1
                res=min(res,right-left+2)
            visted.add(cards[right])
        return res if res<=len(cards) else -1
            