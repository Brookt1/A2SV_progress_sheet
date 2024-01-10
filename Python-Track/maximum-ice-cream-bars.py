class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        max_cost=max(costs)
        counting=[0]*(max_cost+1)
        for cost in costs:
            counting[cost]+=1
        res=0
        idx=1
        while coins>=idx and idx<len(counting):
            if counting[idx]:
                res+=1
                counting[idx]-=1
                coins-=idx
            else:
                idx+=1
        return res

        