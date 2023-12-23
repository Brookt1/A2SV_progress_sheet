class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        res=[]
        gre=max(candies)
        for can in candies:
            if can+extraCandies>=gre:
                res.append(True)
            else:
                res.append(False)
        return res