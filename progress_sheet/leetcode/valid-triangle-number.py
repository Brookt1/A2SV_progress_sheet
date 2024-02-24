class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort(reverse=True)
        ans=0
        for i in range(len(nums)):
            left,right=i+1,len(nums)-1
            while left<right:
                sum=nums[left]+nums[right]
                if sum>nums[i]:
                    ans+=(right-left)
                    left+=1
                else:
                    right-=1
        return ans   