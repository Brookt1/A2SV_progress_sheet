class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        l,r=0,k
        win_sum=sum(nums[:k])
        max_val=win_sum/k
        while r<len(nums):
            win_sum=win_sum-nums[l]+nums[r]
            max_val=max(max_val,win_sum/k)
            l+=1
            r+=1
        return max_val

        