class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        res=0
        while target>1:

            if maxDoubles>0:
                if target%2!=0:
                    res+=1
                target=target//2
                maxDoubles-=1
            else:
                res+=target-1
                break
            res+=1
        return res

