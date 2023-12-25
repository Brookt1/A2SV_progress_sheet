class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=0
        n=len(nums)
        for num in nums:
            sum+=num
        res=n*(n+1)//2-sum
        return res if res>0 else 0
        