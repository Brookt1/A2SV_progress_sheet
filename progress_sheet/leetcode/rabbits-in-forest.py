class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        res=0
        for key,val in count.items():
            res+=ceil(val/(key+1))*(key+1)
        return res
        