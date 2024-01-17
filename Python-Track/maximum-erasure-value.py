class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        res,sum=0,0
        visted=set()
        left=0
        for right in range(len(nums)):
            while nums[right] in visted:
                sum-=nums[left]
                visted.remove(nums[left])
                left+=1
            visted.add(nums[right])
            sum+=nums[right]
            res=max(res,sum)
        return res     
