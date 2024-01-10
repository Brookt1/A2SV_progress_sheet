class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count_flip=0
        bin=[0]*len(flips)
        total=0
        for idx,val in enumerate(flips):
            bin[val-1]=1
            if val<idx+1:total+=1
            if bin[idx]: total+=1
            if total==idx+1:
                count_flip+=1
        return count_flip