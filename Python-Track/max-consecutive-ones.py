class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        res,count=0,0
        for num in nums:
            if num==1: count+=1
            else: count=0
            res=max(count,res)
        return res
