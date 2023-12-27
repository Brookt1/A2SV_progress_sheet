class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        

        nums.sort()
        res=0
        for i in range(len(nums)-2):
            s=(nums[i]+nums[i+1]+nums[i+2])/2
            area=s*(s-nums[i])*(s-nums[i+1])*(s-nums[i+2])
            if area>0: res=nums[i]+nums[i+1]+nums[i+2]
        return res