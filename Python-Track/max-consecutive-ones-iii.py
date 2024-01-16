class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        num_zero=0
        l,r=0,0
        res=0
        while r<len(nums):
            while num_zero==k and nums[r]==0:
                if nums[l]==0:
                    num_zero-=1
                l+=1
            res=max(res,r-l+1)
            if nums[r]==0:
                num_zero+=1
            r+=1
        return res
        