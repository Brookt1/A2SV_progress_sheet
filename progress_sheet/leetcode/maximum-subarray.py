class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        sum=left=0
        res=max(nums)
        for right in range(len(nums)):
            sum+=nums[right]
            while sum<0:
                sum-=nums[left]
                left+=1
            res=max(sum,res)
        
        if res==0:
            return max(nums)
        return res
        