class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        res=sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            res=max(res,ceil(sum/(i+1)))
        return res
