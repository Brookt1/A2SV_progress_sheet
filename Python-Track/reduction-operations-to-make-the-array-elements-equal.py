class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        l,r=len(nums)-2,len(nums)-1
        res=0
        while l>-1:
            if nums[l]==nums[r]:
                l-=1
            else:
                res+=len(nums)-l-1
                r=l
        return res


        