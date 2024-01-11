class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()
        piles.reverse()
        print(piles)
        res=0
        for i in range(1,len(piles)-len(piles)//3,2):
            res+=piles[i]
        return res

        