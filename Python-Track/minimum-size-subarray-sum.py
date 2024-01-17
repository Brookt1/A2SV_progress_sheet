class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left=0
        res,sum=len(nums)+1,0
        for right in range(len(nums)):
            sum+=nums[right]
            while sum>=target:
                res=min(res,right-left+1)
                sum-=nums[left]
                left+=1
        return res if res<=len(nums) else 0





        