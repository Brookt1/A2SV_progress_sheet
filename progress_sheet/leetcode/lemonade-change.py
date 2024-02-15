class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        bala=[0,0,0]
        for bill in bills:
            if bill==5:
                bala[0]+=1
            elif bill==10:
                if bala[0]<1:return False
                bala[0]-=1
                bala[1]+=1
            else:
                if bala[1]>0:
                    bala[1]-=1
                else:
                    bala[0]-=2
                if bala[0]<1: return False
                bala[0]-=1
                bala[2]+=1
        return True

        